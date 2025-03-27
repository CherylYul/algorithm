// Implement Array.prototype functions: map, reduce, filter, sort

// This help us redefine the map method for Array objects, named myMap
if (!Array.prototype.myMap) {
    // 1. Kiểm tra sự tồn tại: đảm bảo rằng AArray.prototype.myMap chưa được định nghĩa trước để tránh conflict
    Array.prototype.myMap = function(callback, thisArg) {
        // 2. Kiểm tra đầu vào: xem mảng this có hợp lệ và callback có phải 1 hàm hay không
        // callback is the function to execute for each element in the array
        // thisArg is the value to use as this when executing callback
        if (this == null) {
            throw new TypeError('Array.prototype.map called on null or undefined')
        }
        if (typeof callback !== 'function') {
            throw new TypeError(callback + ' is not a function')
        }
        // 3. Khởi tạo: chuyển mảng sang object
        // Lấy chiều dài của mảng rồi sử dụng toán tử dịch bit sang phải để đảm bảo chiều dài là 1 số nguyên không âm
        // Tạo 1 mảng mới A có chiều dài như mảng ban đầu để chứa kết quả
        const O = Object(this)
        // Zero-fill right shift operator: dịch sang 0 nghĩa là không có sự dịch chuyển nào xảy ra mà chỉ ép nó không âm
        const len = O.length >>> 0
        const A = new Array(len)

        // 4. Duyệt mảng: gọi hàm callback cho mỗi phần tử, cung cấp giá trị, chỉ số và mảng ban đầu làm đối số.
        let k = 0
        while (k < len) {
            if (k in O) {
                // kiểm tra xem chỉ số 'k' có nằm trong mảng 'O' không
                // quan trọng khi xử lý các mảng thưa (sparse array)
                A[k] = callback.call(thisArg, O[k], k, O)
                // Gọi hàm callback với các tham số sau:
                // - thisArg: giá trị của this khi gọi hàm callback 
                // - O[k]: giá trị của phần tử tại chỉ số k
                // - k: chỉ số hiện tại
                // - O: mảng ban đầu
            }
            k++
        }
        // 5. Trả về mảng mới
        return A
    }

}

const a = [1, 2, 3, 4, 5]
a.map(item => item * 2)

// This help us redefine the reduce method for Array objects, named myReduce
if (!Array.prototype.myReduce) {
    Array.prototype.myReduce = function(callback, initialValue) {
        if (this == null) {
            throw new TypeError('Array.prototype.reduce called on null or undefined')
        }
        if (typeof callback !== 'function') {
            throw new TypeError(callback + ' is not a function')
        }

        const O = Object(this)
        const len = O.length >>> 0
        let accumulator = initialValue
        let k = 0
        // Handle initialValue absence: if initialValue is not provided, 
        // it tries to use the first non-empty element in the array as initialValue
        if (initialValue === undefined) {
            if (len === 0) {
                throw new TypeError('Reduce with empty array with no initial value');
            }
            while (k < len && !(k in O)) k++
            if (k >= len) {
                throw new TypeError('Reduce with empty array with no initial value');
            }
            accumulator = O[k++]
        }

        while (k < len) {
            if (k in O) {
                accumulator = callback.call(undefined, accumulator, O[k], k, O)
            }
            k++
        }
        return accumulator
    }
}

const b = [1, 2, 3, 4, 5]
b.reduce((acc, item) => acc + item, 0)

// This help us redefine the filter method for Array objects, named myFilter
if (!Array.prototype.myFilter) {
    Array.prototype.myFilter = function(callback, thisArg) {
        if (this == null) {
            throw new TypeError('Array.prototype.filter called on null or undefined')
        }
        if (typeof callback !== 'function') {
            throw new TypeError(callback + ' is not a function')
        }

        const O = Object(this)
        const len = O.length >>> 0
        const A = []
        let k = 0
        // Conditional Push: If the callback returns a truthy value, the current element is pushed into the A array.
        while (k < len) {
            if (k in O) {
                if (callback.call(thisArg, O[k], k, O)) {
                    A.push(O[k])
                }
            }
            k++
        }
        return A
    }
}

const c = [1, 2, 3, 4, 5]
c.filter(item => item % 2 === 0)

// This help us redefine the sort method for Array objects, named mySort
if (!Array.prototype.mySort) {
    Array.prototype.mySort = function(compareFn) {
        if (this == null) {
            throw new TypeError('Array.prototype.sort called on null or undefined')
        }

        const O = Object(this)
        const len = O.length >>> 0

        const defaultCompare = (a, b) => {
            const aStr = String(a)
            const bStr = String(b)
            if (aStr === bStr) return 0
            return aStr < bStr ? -1 : 1
        }

        const actualCompareFn = compareFn || defaultCompare

        for (let i = 0; i < len - 1; i++) {
            for (let j = i + 1; j < len; j++) {
                if (actualCompareFn(O[i], O[j]) > 0) {
                    const temp = O[i]
                    O[i] = O[j]
                    O[j] = temp
                }
            }
        }
        return O
    }
}

const d = [1, 3, 5, 2, 4]
d.sort((a, b) => a - b)

const numbers = [1, 5, 2, 8, 3];

const doubled = numbers.myMap(num => num * 2);
console.log("myMap:", doubled); // Output: [ 2, 10, 4, 16, 6 ]

const sum = numbers.myReduce((acc, curr) => acc + curr, 0);
console.log("myReduce:", sum); // Output: 19

const evenNumbers = numbers.myFilter(num => num % 2 === 0);
console.log("myFilter:", evenNumbers); // Output: [ 2, 8 ]

const sortedNumbers = numbers.mySort();
console.log("mySort (default):", sortedNumbers); // Output: [ 1, 2, 3, 5, 8 ]

const sortedDescending = numbers.mySort((a, b) => b - a);
console.log("mySort (descending):", sortedDescending); // Output: [ 8, 5, 3, 2, 1 ]

const words = ["apple", "banana", "cherry"];
const sortedWords = words.mySort();
console.log("mySort (words):", sortedWords); // Output: [ 'apple', 'banana', 'cherry' ]