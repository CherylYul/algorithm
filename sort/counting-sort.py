# Given n integers in the range 0 to k, use counting sort to sort the array
tests = []

tests.append(
    {
        "input": [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2],
        "max": 6,
        "output": [0, 0, 1, 1, 2, 2, 3, 3, 4, 6, 6],
    }
)

"""
Counting sort is stable sort which takes Θ(k+n)
Step 1: create an empty array b with length a, b is responsible to store the sorted array
Step 2: create an empty array c with length c, c is responsible for counting the number of value in a
    ex: a has 2 value 6 and 1 value 0 then c = [1, 0, 0, 0, 0, 0, 2]
Step 3: counting the number of value in a
Step 4: accumulated the counting value in c to signal that at value i we have how many values equal and
    smaller to, ex: a has 2 value 0, 2 value 1, 1 value 2, so at position 2, 
        it will have 5 elements equal or smaller than it, c = [2, 4, 5]
Step 5: based on what we counting, arrange the right position to array b and return it
"""


def counting_sort(a, k):
    b = [0 for _ in range(len(a))]
    c = [0 for _ in range(k + 1)]
    for i in range(len(a)):
        c[a[i]] += 1
    # print(c)
    for i in range(1, k + 1):
        c[i] += c[i - 1]
    # print(c)
    for i in range(len(a)):
        b[c[a[i]] - 1] = a[i]
        c[a[i]] -= 1
    return b


print(counting_sort(tests[0]["input"], tests[0]["max"]))
