/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length !== t.length) return false
    counter_s = new Array(26).fill(0)
    counter_t = new Array(26).fill(0)
    const start = 'a'.charCodeAt(0)
    for (let i=0; i<s.length; i++) {
        counter_s[s.charCodeAt(i) - start] += 1
        counter_t[t.charCodeAt(i) - start] += 1
    }
    console.log(counter_s)
    console.log(counter_t)
    return counter_s.toString() === counter_t.toString()
};