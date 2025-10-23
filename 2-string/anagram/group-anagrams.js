/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let hashMap = {}
    for (const s of strs) {
        const key = s.split("").sort().join("")
        if (!hashMap[key]) hashMap[key] = []
        hashMap[key].push(s)
    }
    return Object.values(hashMap)
};