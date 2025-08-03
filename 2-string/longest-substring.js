/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let best = 0
    let l = 0
    let curr = 0
    let hashTable = new Array(26).fill(false)
    const start = 'a'.charCodeAt(0)
    for (let i=0; i<s.length; i++) {
        const pos = s.charCodeAt(i)-start
        if (!hashTable[pos]) {
            hashTable[pos] = true
            curr++;
            best = Math.max(curr,best)
        } else {
            while (s[l] !== s[i]) {
                hashTable[s.charCodeAt(l)-start] = false
                curr--; l++;
            }
            l++;
        }
    }
    return best
};