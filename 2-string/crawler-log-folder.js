/**
 * @param {string[]} logs
 * @return {number}
 */
var minOperations = function(logs) {
    let count = 0
    for (let log of logs) {
        if (log === "../") count = count > 0 ? count-1 : count
        else if (log !== "./") count++
    }
    return count
};