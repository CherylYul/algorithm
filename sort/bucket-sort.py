tests = []

tests.append(
    {
        "input": [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68],
        "output": [0.12, 0.17, 0.21, 0.23, 0.26, 0.39, 0.68, 0.72, 0.78, 0.94],
    }
)

tests.append(
    {
        "input": [0.79, 0.13, 0.16, 0.64, 0.39, 0.20, 0.89, 0.53, 0.71, 0.72],
        "output": [0.13, 0.16, 0.20, 0.39, 0.53, 0.64, 0.71, 0.72, 0.79, 0.89],
    }
)

"""
Bucket sort assumes the input is drawn from a uniform distribution and
has an average case running time of O(n)
Step 1: construct an empty array b, b is divided into n equal-sized buckets
Step 2: distribute the n input numbers into the buckets
Step 3: sort each bucket with insertion sort, go through the buckets in order,
list them and return

The worst case happens, O(n^2) when all input fall into one bucket. In that case,
we can change to use merge sort or heap sort to improve the running time
"""


def bucket_sort(a):
    b = [[] for _ in range(10)]
    for v in a:
        b[int(10 * v)].append(v)
    result = []
    for i in range(10):
        b[i] = insertion_sort(b[i])
        result.extend(b[i])
    return result


def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        current_pos = i - 1
        current = a[i]
        while current_pos >= 0 and current < a[current_pos]:
            a[current_pos + 1] = a[current_pos]
            current_pos -= 1
        a[current_pos + 1] = current
    return a


print(bucket_sort(tests[1]["input"]))
