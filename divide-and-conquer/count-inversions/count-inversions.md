## Problems

2 people rank favorite to least favorite given a list of n movies on Netflix. Are their tastes similar?

<hr>

## Idea

To find similarity between rankings is to do collaborative filtering, a technique for generating recommendations based on similar preferences.

We can start a list of n elements, this list means if first people most favorite films in the fifth position of another then A[1] = 5, if the 2 rankings are identical means this array is sorted and have no inversions.

So to measure that tastes between 2 people means to count the inversions in array. The more inversions the array has, the more pair of movies on which one disagree with their relative merits and the more different on preferences

To count inversions, we can based on the algorithms inplemented in merge sort. When combining the merge of 2 arrays, if the element in right arrays is smaller than the element in left array, which means the remains element in the left is larger than the element in the right (since left and right array is already sorted before), so we can conclude that the remains element in the left is the number of inversions.

```
Initial array:      2, 3, 8, 6, 1
Divide:         2, 3         8, 6, 1
                        .
                        .
                        .
Conquer:        2, 3         1, 6, 8
    1 smaller than 2 so we add 1 to new array, 1 in right array and left has 2 elements inversion + 2
    2 smaller than 6 so we add 2 to new array, 2 in the left so we don't care about the inversions
    Similarly, 3 smaller than 6, inversions unchange, then we add 6 and 8 to finish the conquer step
```

<hr>

## Steps

Step 1: If the len of array is smaller than 2 then return no inversions

Step 2: Divide the list into 2 parts, then recursively find inversions of left array and right array

Step 3: Find the inversions when merge the 2 array together (combine steps)

Step 4: Returns the total inversions in 2 arrays

<hr>

## Analysis

$$T(n) = 2T(\frac{n}{2}) + Θ(n)$$

$a=2$

$b=2$

$f(n) = Θ(n)$

$n^{log_ba} = n^{log_22} = n^{1}$

According to Master theorem: $T(n) = Θ(nlogn)$