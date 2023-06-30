### Comparisons among lists

||unsorted, singly linked|sorted, singly linked|unsorted, doubly linked| sorted, doubly linked|
|:-:|:-:|:-:|:-:|:-:|
|`SEARCH(L,k)`|linear|linear|linear|linear|
|`INSERT(L,x)`|constant|linear|constant|linear|
|`DELETE(L,x)`|linear|linear|constant|constant|
|`SUCCESSOR(L,x)`|linear|constant|linear|constant|
|`PREDECESSOR(L,x)`|linear|linear|linear|constant|
|`MINIMUM(L,k)`|linear|constant|linear|constant|
|`MAXIMUM(L,k)`|linear|linear|linear|linear|

### Comparisons among heap, list, array, and binary search tree

|Operation|Heap|Linked list|Sorted array|Balanced BST|
|:-:|:-:|:-:|:-:|:-:|
|Search|Θ(logn)|Θ(n)|Θ(logn)|Θ(logn)|
|Delete|Θ(logn)|Θ(n)|Θ(n)|Θ(logn)|
|Insert|Θ(logn)|Θ(1)|Θ(n)|Θ(logn)|
|Rank|Θ(nlogn)|Θ(n)|Θ(logn)|
|Select (find 5th smallest elements)|Θ(nlogn)|Θ(n)|Θ(1)|
|Predecessor & Sucessor|Θ(1)|Θ(n)|Θ(1)|Θ(logn)|

sorted in o(n) bst


**Binary search tree**: left is smaller than node, and the right is larger than the node (imagine the node like the pivot in quicksort)

- Running time of search, insert, delete is based on height of tree
- worst case: unbalanced tree, this situation can happend when insert make increase the height of the tree every time it is called, leading to worst case O(n)
- best case: balanced tree. O(logn)

**Red black tree**: all leaves are assumed to have NILs as children
1. Every node is red or black
2. The root is black
3. NILs are black
4. The children of a red node are black
5. For every node x, all x to NIL paths have the same number of black nodes on them

- height <= $2log_2(n+1)$ = O(logn)
- O(logn)