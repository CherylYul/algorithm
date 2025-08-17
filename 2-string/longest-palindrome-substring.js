/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    if (s.length === 1) return s
    let longestStr = s[0]
    if (s[0] === s[1]) longestStr = s.slice(0,2)
    for (let i=1; i<s.length-1; i++) {
        let strOdd = checkPalindrome(i-1,i+1,s)
        if (strOdd.length > longestStr.length) longestStr = strOdd
        if (s[i] === s[i+1]) {
            let strEven = checkPalindrome(i-1,i+2,s)
            if (strEven.length > longestStr.length) longestStr = strEven
        }
        if (longestStr.length > (s.length - i)*2 ) return longestStr;
    }
    return longestStr
};

var checkPalindrome = function(l, r, s) {
    while (l >= 0 && r < s.length && s[l] === s[r]) {
        l--;
        r++
    }
    return s.slice(l+1,r)
}