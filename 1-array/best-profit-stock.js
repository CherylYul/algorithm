/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let pointer = 0
    let best = 0
    for (let i = 0; i < prices.length; i++) {
        let profit = prices[i] - prices[pointer]
        if (profit > best) {
            best = profit
        }
        if (profit < 0) {
            pointer = i
        }
    }
    return best
};