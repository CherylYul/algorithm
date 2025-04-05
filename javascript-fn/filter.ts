interface Array<T> {
  myFilter(
    callbackFn: (value: T, index: number, array: Array<T>) => boolean,
    thisArg?: any
  ): Array<T>;
}

Array.prototype.myFilter = function (callbackFn, thisArg) {
  const len = this.length;
  const results: any[] = [];

  for (let k = 0; k < len; k++) {
    const kValue = this[k];
    if (
      // Ignore index if value is not defined for index (e.g. in sparse arrays). [1, 2, , 4]
      Object.hasOwn(this, k) &&
      callbackFn.call(thisArg, kValue, k, this)
    ) {
      results.push(kValue);
    }
  }

  return results;
};

// 1. initial new array to store results
// 2. loop through the array via this, callback (element, index, array)
// 3. store the value before callback, because callback can change the value of this (context)
// 4. check sparse array, and if the callback true

// thisArg kiểm soát ngữ cảnh của hàm thực thi, nếu không thì sẽ là undefined, window, global
// const numbers = [1, 5, 10, 15, 20];
// const counter = new Counter(10);
// const filteredNumbers1 = numbers.myFilter(function(num) {
//   // 'this' ở đây sẽ là undefined (trong strict mode) hoặc window/global
//   return num > this.count; // Lỗi: không thể đọc thuộc tính 'count' của undefined
// });
// const filteredNumbers2 = numbers.myFilter(function(num) {
//   return num > this.count; // 'this' ở đây sẽ là đối tượng 'counter'
// }, counter);
