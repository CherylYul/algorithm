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

tests.append(
    {
        "input": [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1],
        "output": [0, 1, 2, 4, 5, 6, 7, 8, 9, 12, 13, 15],
    }
)


def parent(i):
    return (i + 1) / 2 - 1  # parent = i / 2


def left(i):
    return (i + 1) * 2 - 1  # left = i * 2


def right(i):
    return (i + 1) * 2  # right = i * 2 + 1


def last_node(a):
    return len(a) - 1


# Heap sort

# O(logn)
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
    return a


# O(n)
def build_max_heap(a):
    mid = len(a) / 2 - 1
    for i in range(mid, -1, -1):
        max_heapify(a, i)


def build_min_heap(a):
    mid = len(a) / 2 - 1
    for i in range(mid, -1, -1):
        min_heapify(a, i)


# O(nlogn)
def heapsort_increase(a):
    build_max_heap(a)
    for i in range(len(a) - 1, 1, -1):
        a[i], a[0] = a[0], a[i]
        a[:i] = max_heapify(a[:i], 0)
    a[0], a[1] = a[1], a[0]
    return a


def heapsort_decrease(a):
    build_min_heap(a)
    for i in range(len(a) - 1, 1, -1):
        a[i], a[0] = a[0], a[i]
        a[:i] = min_heapify(a[:i], 0)
    a[0], a[1] = a[1], a[0]
    return a


# priority queues


def heap_maximum(a):
    return a[0]


def heap_minimum(a):
    return a[0]


def heap_extract_max(a):
    if last_node(a) < 0:
        print("heap underflow!")
    heap_max, a[0] = a[0], a[last_node(a)]
    a = max_heapify(a[: last_node(a)], 0)
    return heap_max, a


def heap_extract_min(a):
    if last_node(a) < 0:
        print("heap underflow!")
    heap_min, a[0] = a[0], a[last_node(a)]
    a = min_heapify(a[: last_node(a)], 0)
    return heap_min, a


# change the value a[i] to key and recheck the parent node
def heap_increase_key(a, i, key):
    if key < a[i]:
        print("new key is smaller than current key!")
    a[i] = key
    while i > 0 and a[parent(i)] < a[i]:
        a[i], a[parent(i)] = a[parent(i)], a[i]
        i = parent(i)
    return a


def heap_decrease_key(a, i, key):
    if key > a[i]:
        print("new key is larger than current key!")
    a[i] = key
    while i > 0 and a[i] < a[parent(i)]:
        a[i], a[parent(i)] = a[parent(i)], a[i]
        i = parent(i)
    return a


def max_heap_insert(a, key):
    a.append(-float("inf"))
    return heap_increase_key(a, len(a) - 1, key)


def min_heap_insert(a, key):
    a.append(float("inf"))
    return heap_decrease_key(a, len(a) - 1, key)


def heap_delete(a, i):
    if a[i] > a[last_node(a)]:
        a[i] = a[last_node(a)]
        max_heapify(a, i)
    else:
        heap_increase_key(a, i, a[last_node(a)])
    a = a[: last_node(a)]
    return a


print(heapsort_increase(tests[1]["input"]))
print(heapsort_decrease(tests[1]["input"]))
a = heapsort_decrease(tests[1]["input"])
print(max_heap_insert(a, 15))
print(heap_extract_max(tests[2]["input"]))
print(heap_delete([89, 25, 35, 19, 22, 29, 20, 2, 5, 21, 7, 26], 4))
print(heap_delete([89, 25, 35, 19, 22, 25, 20, 2, 5, 21, 6, 17, 20], 4))
