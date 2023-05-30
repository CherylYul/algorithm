<h2>Problem</h2>
<p>Invest in company XYZ, allow to buy 1 unit of stock only 1 time and sell it later date, buying and selling after the close of trading for the day. If we know the price of the stock in the future, write an algorithm that maximize the profit,</p>

<p>For instance, the maximum profit for buying and selling 1 time of this stock over a 17-day period is 43$</p>

|Day|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|Price|100|113|110|85|105|102|86|63|81|101|94|106|101|79|94|90|97
|Change||13|-3|-25|20|-3|-16|-23|18|20|-7|12|-5|-22|15|-4|7

<hr>

<h2>Idea</h2>
<p>If we use brute force, we will try possible pairs of buying and selling dates which takes n square times.</p>

<p>Instead of looking at the price of stock, we can look at the change of each day, then apply the divide and conquer paradigm to calculate the maximum profit between subarray</p>

<hr>

<h2>Steps</h2>

1. Convert the price per day of stock into the change each day with n-1 length
2. Divide problem: recursively divide the array into half, solve the subproblems left and right
3. Handle base case: for minimum size, only has 1 change between the price of 2 days, so return it as the max profit
4. Combine the problem: find the maximum profit from the middle day back + from the middle day to, then sum it together.
5. Compare the maximum profit of left, right and combine case

<hr>

<h2>Analysis</h2>

$$T(n)= operations.levels$$
$$T(n) = 2T(\frac{n}{2}) + Θ(n)$$
$$T(n) = nlogn$$