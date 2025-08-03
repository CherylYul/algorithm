/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    s = s.toLowerCase().replace(/[^a-z0-9]/g, '')
    let l = 0
    let r = s.length - 1
    while (r > l) {
        if (s[r] !== s[l]) return false
        l++; r--;
    }
    return true
};