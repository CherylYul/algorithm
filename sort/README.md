**Running times of sorting algorithms**

|Algorithm|Worst-case running time|Average-case Expected running time
|:-:|:-:|:-:|
|Insertion sort|$Θ(n^2)$|$Θ(n^2)$
|Merge sort|$Θ(nlogn)$|$Θ(nlogn)$
|Heap sort|$O(nlogn)$|-
|Quick sort|$Θ(n^2)$|$Θ(nlogn)$
|Counting sort|$Θ(k+n)$|$Θ(k+n)$
|Radix sort|$Θ(d(n+k))$|$Θ(d(n+k))$
|Bucket sort|$Θ(n^2)$|$Θ(n)$

**Quick sort vs Merge sort**

||Quick sort (random pivot)|Merge sort (deterministic)|
|:-:|:-:|:-:|
|Running time|Worst case: $O(n^2)$ <hr> Expected: $O(nlogn)$|Worst case: $O(nlogn)$|
|In place|Yes|No|
|Stable|No|Yes|
|Pros|Good cache locality if implemented for arrays|Efficient with linked lists|