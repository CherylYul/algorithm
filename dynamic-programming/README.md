## What is dynamic programming?

Dynamic programming is used for solving optimization problems by keep updating the solution table dynamically

**Optimal Substructure**

- Fibonacci: $F(i) = F(i-2) + F(i-1)$
- Bellman-Ford: $d^{i+1}[v] = min(d^{i}[v], d^{i}[u] + w(u,v))$

**Overlapping sub-problems**

- Fibonacci: both F[i-1] and F[i-2] use F[i]
- Bellman-Ford: many different entries of $d^{i+1}$ will use $d^{i}[v]$

## How to solve it?

1. Bottom-up: fill in the table starting with the smallest subproblems. Then,
   assuming that we have computed the optimal solution to small subproblems, we can
   compute the answers for larger subproblems using our recursive optimal substructure.
   (dynamic programming)

2. Top-down: compute the optimal solution to the entire problem recursively. At each
   recursive call, we will end up looking up the answer or filling in the table if the
   entry has not been computed yet.
   (memoization)
