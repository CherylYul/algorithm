/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    let hIndex = 0
    citations.sort((a,b)=>a-b)
    for (let i=0; i<citations.length; i++) {
        if (citations.length-i <= citations[i]) return citations.length-i
        else hIndex = citations[i]
    }
    return hIndex
};