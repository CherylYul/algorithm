## Sorting

|   Algorithm    | Worst-case  | Average-case |   Space   |
| :------------: | :---------: | :----------: | :-------: |
|  Bubble sort   |  $Θ(n^2)$   |   $Θ(n^2)$   |  $Θ(1)$   |
| Insertion sort |  $Θ(n^2)$   |   $Θ(n^2)$   |  $Θ(1)$   |
| Selection sort |  $Θ(n^2)$   |   $Θ(n^2)$   |  $Θ(1)$   |
|   Merge sort   | $Θ(nlogn)$  |  $Θ(nlogn)$  |  $Θ(n)$   |
|   Quick sort   |  $Θ(n^2)$   |  $Θ(nlogn)$  | $Θ(logn)$ |
|   Heap sort    | $O(nlogn)$  |  $Θ(nlogn)$  |  $Θ(1)$   |
| Counting sort  |  $Θ(k+n)$   |   $Θ(k+n)$   |  $Θ(k)$   |
|   Radix sort   | $Θ(d(n+k))$ | $Θ(d(n+k))$  | $Θ(n+k)$  |
|  Bucket sort   |  $Θ(n^2)$   |    $Θ(n)$    | $Θ(n+k)$  |

## Compare Quick sort vs Merge sort

|              |           Quick sort (random pivot)            | Merge sort (deterministic)  |
| :----------: | :--------------------------------------------: | :-------------------------: |
| Running time | Worst case: $O(n^2)$ <hr> Expected: $O(nlogn)$ |   Worst case: $O(nlogn)$    |
|   In place   |                      Yes                       |             No              |
|    Stable    |                       No                       |             Yes             |
|     Pros     | Good cache locality if implemented for arrays  | Efficient with linked lists |

## Comparisons among lists

|                    | unsorted, singly linked | sorted, singly linked | unsorted, doubly linked | sorted, doubly linked |
| :----------------: | :---------------------: | :-------------------: | :---------------------: | :-------------------: |
|   `SEARCH(L,k)`    |         linear          |        linear         |         linear          |        linear         |
|   `INSERT(L,x)`    |        constant         |        linear         |        constant         |        linear         |
|   `DELETE(L,x)`    |         linear          |        linear         |        constant         |       constant        |
|  `SUCCESSOR(L,x)`  |         linear          |       constant        |         linear          |       constant        |
| `PREDECESSOR(L,x)` |         linear          |        linear         |         linear          |       constant        |
|   `MINIMUM(L,k)`   |         linear          |       constant        |         linear          |       constant        |
|   `MAXIMUM(L,k)`   |         linear          |        linear         |         linear          |        linear         |

## Comparisons among heap, list, array, and binary search tree

|              Operation              |   Heap   | Linked list | Sorted array | Balanced BST |
| :---------------------------------: | :------: | :---------: | :----------: | :----------: |
|               Search                | Θ(logn)  |    Θ(n)     |   Θ(logn)    |   Θ(logn)    |
|               Delete                | Θ(logn)  |    Θ(n)     |     Θ(n)     |   Θ(logn)    |
|               Insert                | Θ(logn)  |    Θ(1)     |     Θ(n)     |   Θ(logn)    |
|                Rank                 | Θ(nlogn) |    Θ(n)     |   Θ(logn)    |
| Select (find 5th smallest elements) | Θ(nlogn) |    Θ(n)     |     Θ(1)     |
|       Predecessor & Sucessor        |   Θ(1)   |    Θ(n)     |     Θ(1)     |   Θ(logn)    |
