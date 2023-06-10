### Running times of sorting algorithms

|Algorithm|Worst-case running time|Average-case Expected running time
|:-:|:-:|:-:|
|Insertion sort|$Θ(n^2)$|$Θ(n^2)$
|Merge sort|$Θ(nlogn)$|$Θ(nlogn)$
|Heap sort|$O(nlogn)$|-
|Quick sort|$Θ(n^2)$|$Θ(nlogn)$
|Counting sort|$Θ(k+n)$|$Θ(k+n)$
|Radix sort|$Θ(d(n+k))$|$Θ(d(n+k))$
|Bucket sort|$Θ(n^2)$|$Θ(n)$

**Priority queues**

We can use max-priority queue to keep track of the jobs to be performed on a shared computer based on their relative priorities. When a job is finished or interrupted, the scheduler selects the highest-priority job from among those pending by calling EXTRACT-MAX

**Event Driven Simulator**

The items in the queue are events to be simulated and each associated with time serves as key, the termination of first event cause next event to occur by calling EXTRACT-MIN (computer choose next event to simulate), when the event finished, it was inserted to the min-priority queue by calling INSERT