/**
 * @param {string} s
 * @return {number}
 */
var minLength = function(s) {
    let stack = []
    for (let char of s){
        if (stack.length > 0 && ['AB','CD'].includes(stack.at(-1)+char)) {
            stack.pop()
        } else {
            stack.push(char)
        }
    }
    return stack.length
};