class Heap:
    def __init__(self, a):
        self.arr = a

    def parent(self, i):
        return (i + 1) / 2 - 1

    def left(self, i):
        return (i + 1) * 2 - 1

    def right(self, i):
        return (i + 1) * 2

    def last_node(self):
        return len(self.arr) - 1

    # O(logn)
    def min_heapify(self, i):
        l, r = self.left(i), self.right(i)
        smallest = i
        if l < len(self.arr) and self.arr[l] < self.arr[i]:
            smallest = l
        if r < len(self.arr) and self.arr[r] < self.arr[smallest]:
            smallest = r
        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            self.min_heapify(smallest)
        return self.arr

    # O(nlogn)
    def build_min_heap(self):
        mid = len(self.arr) / 2 - 1
        for i in range(mid, -1, -1):
            self.min_heapify(i)

    # O(logn)
    def heap_extract_min(self):
        if self.last_node() < 0:
            print("heap underflow!")
        heap_min, self.arr[0] = self.arr[0], self.arr[self.last_node()]
        self.arr = self.arr[:-1]
        self.arr = self.min_heapify(0)
        return heap_min

    # O(logn): change the value a[i] to key and recheck the parent node
    def heap_decrease_key(self, i, key):
        if key > self.arr[i]:
            print("new key is larger than current key!")
        self.arr[i] = key
        while i > 0 and self.arr[i] < self.arr[self.parent(i)]:
            self.arr[i], self.arr[self.parent(i)] = (
                self.arr[self.parent(i)],
                self.arr[i],
            )
            i = self.parent(i)
        return self.arr

    # O(logn)
    def min_heap_insert(self, key):
        self.arr.append(float("inf"))
        return self.heap_decrease_key(self.last_node(), key)

    # O(logn)
    def heap_delete(self, i):
        if self.arr[i] < self.arr[self.last_node()]:
            self.arr[i] = self.arr[self.last_node()]
            self.min_heapify(i)
        else:
            self.heap_decrease_key(i, self.arr[self.last_node()])
        self.arr = self.arr[: self.last_node()]
        return self.arr

    def __repr__(self):
        return "Heap {}".format(self.arr)

    def __str__(self):
        return self.__repr__()


H = Heap([32, 21, 3, 46, 29, 13, 55, 10])
H.build_min_heap()
print(H)
print(H.heap_extract_min())
print(H)
print(H.min_heap_insert(15))
print(H.heap_delete(4))
