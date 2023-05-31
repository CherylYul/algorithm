## Problem
For nxn matrix multiplication, it needs Θ($n^3$) when do normal brute-force search to find out the result

```
n = A.rows
C = n x n new matrix
for i = 1 to n
    for j = 1 to n
        c_ij = 0
        for k = 1 to n
            c_ij = c_ij + A[i][k] * B[k][j]
return C
```

<hr>

## Strassen Approach
When using divide and conquer, we divide matrix into n/2 size which causing 8 subproblems, according to Master theorem, $T(n) = 8T(n/2) + Θ(n^2) = Θ(n^3)$, so divide and conquer don't help much.

Strassen eliminates 1 matrix multiplication, instead of 8 recursions, it only performs 7:

Step 1: Divide input matrix A, B and output matrix C into n/2 submatrices, costs $Θ(1)$

Step 2: Create 10 matrices S which is n/2, costs $Θ(n^2)$

$S_1 = B_{12} - B_{22}$

$S_2 = A_{11} + A_{12}$

$S_3 = A_{21} + A_{22}$

$S_4 = B_{21} - B_{11}$

$S_5 = A_{11} + A_{22}$

$S_6 = B_{11} + B_{22}$

$S_7 = A_{12} - A_{22}$

$S_8 = B_{21} + B_{22}$

$S_9 = A_{11} - A_{21}$

$S_{10} = B_{11} + B_{12}$

Step 3: Use matrix S created in step 2, recursively compute 7 matrix products

$P_1 = A_{11} . S_1$

$P_2 = S_2 . B_{22}$

$P_3 = S_3 . B_{11}$

$P_4 = A_{22} . S_4$

$P_5 = S_5 . S_6$

$P_6 = S_7 . S_8$

$P_7 = S_9 . S_{10}$

Step 4: Compute the desired submatrices of the result matrix C, costs $Θ(n^2)$

$C_{11} = P_5 + P_4 - P_2 + P_6$

$C_{12} = P_1 + P_2$

$C_{21} = P_3 + P_4$

$C_{22} = P_5 + P_1 - P_3 - P_7$

<hr>

## Analysis

$$T(n) = 7T(\frac{n}{2}) + Θ(n^2)$$

$a = 7$

$b = 2$

$f(n) = Θ(n^2)$

$n^{log_ba} = n^{log_72} = n^{2.81}$

So $T(n) = Θ(n^{2.81})$