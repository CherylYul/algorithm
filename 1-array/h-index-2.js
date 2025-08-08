/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    let l = 0
    let r = citations.length - 1
    let hIndex = 0
    while (l<=r) {
        let mid = Math.floor((l+r) / 2)
        if (citations.length - mid === citations[mid]) return citations[mid]
        if (citations.length - mid < citations[mid]) {
            hIndex = Math.max(hIndex,citations.length-mid)
            r = mid - 1
        } else {
            hIndex = Math.max(hIndex,citations[mid])
            l = mid + 1
        }
    }
    return hIndex
};