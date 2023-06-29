<h2>Problem</h2>
<p>Given an n by n grid of distinct numbers. A number is a local minimum if it is smaller than all of its neighbors. (A neighbor of a number is one immediately above, below, to the left, or the right). Find a local minimum in n x n matrix in O(n) time.</p>
<hr>

<h2>Idea</h2>
<p>Turn the problem into 3D, imagine there is a ball in the valley, it will always fall into the lower until it reaches local minimum.</p>

<b>Where should the ball start?</b>

<p>If the ball starts at the upper left or upper right, it just has 2-3 neighbors, and takes lots of time to reach all the points in matrix, ex. What if the ball starts at upper left when local minimum at the bottom right?</p>

<p>Best approach is that the ball starts at the smallest element at the middle column and middle row. Then roll one step "downhill" from there to enter one of the four quadrants. </p>

<hr>

<h2>Steps</h2>

1. Divide the n x x matrix into 4 n/2 x n/2 sub matrices
2. At each iterations, we need to keep track of current minimum element, then compare the minimum value of next middle row & column with the previous one we kept track
3. If the smaller one in the middle row & middle column, recurse to the quadrant with smaller altitude. If the smaller one in the element we keep track, recurse into the quadrant containing minimum candidate
4. Continue until we reach the base case: 2 x 2 matrix
5. Check if any 2 x 2 matrix is local minimum

| | | | | | | | | | | |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | 
| x | x | 39 | x | x | 50 | x | x | x | x | x |
| x | x | 38 | x | x | 49 | x | x | x | x | x |
| 37 | 36 | 33 | 34 | 35 | 48 | x | x | x | x | x |
| x | x | 32 | x | 1 | 10 | x | x | x | x | x |
| x | x | 31 | x | x | 47 | x | x | x | x | x |
| 46 | 45 | 30 | 44 | 43 | 60 | 51 | 52 | 53 | 54 | 55 |
| x | x | 2 | x | x | 56 | x | x | x | x | x |
| x | x | 2 | x | x | 57 | x | x | x | x | x |
| x | x | 2 | x | x | 58 | x | x | x | x | x |
| x | x | 2 | x | x | 59 | x | x | x | x | x |

<hr>

<h2>Analysis</h2>

$$T(n) = T(\frac{n}{2}) + cn$$
$$T(n) = T(\frac{n}{4}) + c\frac{n}{2} + cn$$
$$T(n) = T(\frac{n}{8}) + c\frac{n}{4} + c\frac{n}{2} + cn$$
$$T(n) = T(1) + c(1 + 2 + 4 + ... + \frac{n}{4} + \frac{n}{2} + n)$$
$$T(n) = T(1) + Θ(n)$$
