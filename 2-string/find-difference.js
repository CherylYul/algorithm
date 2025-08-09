/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function(s, t) {
    let hashMap = {}
    const n = s.length
    for (let i=0; i<n; i++) {
        hashMap[s[i]] = (hashMap[s[i]] || 0) - 1
        hashMap[t[i]] = (hashMap[t[i]] || 0) + 1
    }
    hashMap[t[n]] = (hashMap[t[n]] || 0) + 1
    for (let char in hashMap) {
        if (hashMap[char] > 0) return char
    }
};

var findTheDifference = function(s, t) {
    let total = 0
    for (const char of s) total -= char.charCodeAt(0)
    for (const char of t) total += char.charCodeAt(0)
    return String.fromCharCode(total)
};

var findTheDifference = function(s, t) {
    let charNo = 0
    for (let i=0; i<s.length; i++) charNo ^= s.charCodeAt(i) ^ t.charCodeAt(i)
    charNo ^= t.charCodeAt(s.length)
    return String.fromCharCode(charNo)
};