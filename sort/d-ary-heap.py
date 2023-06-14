import math

tests = []

tests.append(
    {
        "input": [5, 3, 17, 10, 84, 19, 6, 22, 9],
        "output": [3, 5, 6, 9, 10, 17, 19, 22, 84],
    }
)

# d-ARY
def d_ary_parent(d, i):
    return int(math.floor((i - 1) / d))  # (i-2)/d + 1


def d_ary_child(d, i, j):
    return int(d * i + j)  # d(i-1) + j + 1


# O(dlog_d(n))
def d_ary_max_heapify(d, a, i):
    largest = i
    for k in range(d):
        child = d_ary_child(d, i, k + 1)
        if child < len(a) and a[child] > a[largest]:
            largest = child
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        d_ary_max_heapify(d, a, largest)
    return a


def build_d_ary_max_heap(d, a):
    mid = len(a) / d - 1
    for i in range(mid, -1, -1):
        d_ary_max_heapify(d, a, i)


def d_ary_extract_max(d, a):
    if len(a) < 1:
        print("heap underflow!")
    heap_max, a[0] = a[0], a[len(a) - 1]
    a = d_ary_max_heapify(d, a[: len(a) - 1], 0)
    return heap_max


def d_ary_max_heap_insert(d, a, key):
    a.append(-float("inf"))
    return d_ary_heap_increase_key(d, a, len(a) - 1, key)


# change the value a[i] to key and recheck the parent node
def d_ary_heap_increase_key(d, a, i, key):
    if key < a[i]:
        print("new key is smaller than current key!")
    a[i] = key
    while i > 0 and a[d_ary_parent(d, i)] < a[i]:
        a[i], a[d_ary_parent(d, i)] = a[d_ary_parent(d, i)], a[i]
        i = d_ary_parent(d, i)
    return a


print(build_d_ary_max_heap(4, tests[0]["input"]))
a = d_ary_max_heapify(4, tests[0]["input"], 0)
print(a)
print(d_ary_max_heap_insert(4, tests[0]["input"], 100))
