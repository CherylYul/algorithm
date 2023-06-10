tests = []

tests.append(
    {
        "input": [5, 3, 17, 10, 84, 19, 6, 22, 9],
        "output": [3, 5, 6, 9, 10, 17, 19, 22, 84],
    }
)

tests.append(
    {
        "input": [16, 14, 10, 8, 7, 9, 3, 2, 4, 1],
        "output": [1, 2, 3, 4, 7, 8, 9, 10, 14, 16],
    }
)


def parent(i):
    return i / 2


def left(i):
    return i * 2


def right(i):
    return i * 2 + 1


# Heap sort


def max_heapify(a, i):
    l, r = left(i), right(i)
    largest = i
    if l < len(a) and a[l] > a[i]:
        largest = l
    if r < len(a) and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[largest], a[i] = a[i], a[largest]
        max_heapify(a, largest)
    return a


def min_heapify(a, i):
    l, r = left(i), right(i)
    smallest = i
    if l < len(a) and a[l] < a[i]:
        smallest = l
    if r < len(a) and a[r] < a[smallest]:
        smallest = r
    if smallest != i:
        a[smallest], a[i] = a[i], a[smallest]
        min_heapify(a, smallest)


def build_max_heap(a):
    mid = len(a) / 2 - 1
    for i in range(mid, -1, -1):
        max_heapify(a, i)


def build_min_heap(a):
    mid = len(a) / 2 - 1
    for i in range(mid, -1, -1):
        min_heapify(a, i)


def heapsort(a):
    build_max_heap(a)
    for i in range(len(a) - 1, 1, -1):
        a[i], a[0] = a[0], a[i]
        a[:i] = max_heapify(a[:i], 0)
    a[0], a[1] = a[1], a[0]
    return a


# Max priority queues


def heap_maximum(a):
    return a[0]


def max_heap_insert():
    pass


def heap_extract_max(a):
    last_node = len(a) - 1
    if last_node < 0:
        print("heap underflow!")
    heap_max, a[0] = a[0], a[last_node]
    a = a[:last_node]
    max_heapify(a, 0)
    return heap_max


def heap_increase_key():
    pass


# Min priotity queues


def heap_minimum(a):
    return a[0]


print(heapsort(tests[0]["input"]))
print(heap_extract_max([55, 22, 44, 23, 1, 32, 4]))
