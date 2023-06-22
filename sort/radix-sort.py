import string

tests = []
tests.append(
    {
        "input": [329, 457, 657, 839, 436, 720, 355],
        "digit": 3,
        "output": [329, 355, 436, 457, 657, 720, 839],
    }
)

tests.append(
    {
        "input": [
            "COW",
            "DOG",
            "SEA",
            "RUG",
            "ROW",
            "MOB",
            "BOX",
            "TAB",
            "BAR",
            "EAR",
            "TAR",
            "DIG",
            "BIG",
            "TEA",
            "NOW",
            "FOX",
        ],
        "digit": 3,
        "output": [
            "BAR",
            "BIG",
            "BOX",
            "COW",
            "DIG",
            "DOG",
            "EAR",
            "FOX",
            "MOB",
            "NOW",
            "ROW",
            "RUG",
            "SEA",
            "TAB",
            "TAR",
            "TEA",
        ],
    }
)

"""
Radix sort sorts on the least significant digit first with another stable sort
ex: sort dates by three keys: dates, month, then year
insertion sort, merge sort & counting sort are stable; heapsort & quicksort are not

Say we want to sort n integers, size M, base r, number iterations in radix sort:
d = log_r(M) + 1. We put n items into r buckets, so running time is O(d(n+r)) =
O((log_r(M) + 1).(n+r))

Pick base: should choose r = n, running time: O(2n.(log_r(M) + 1))

Running time also depends on size M:
1. if M <= n^c, running time: O(n)
2. if M = 2^n, running time: O(\frac{n^2}{logn})

=> Radix sort can sort n integers of size at most n^100 in time O(n), but needs
enough space to store O(n) integers. However, we should avoid case that size much
bigger than n like 2^n
"""


def radix_sort_on_digit(a, d):
    for i in range(1, d + 1):
        a = counting_sort_on_digit(a, i)
    return a


def radix_sort_on_word(a, letter_nums):
    for i in range(letter_nums - 1, -1, -1):
        a = counting_sort_on_word(a, i)
    return a


def counting_sort_on_digit(a, d):
    div = 10 ** (d - 1)
    c = [0 for _ in range(10)]
    b = a[:]
    for i in a:
        digit = (i // div) % 10
        c[digit] += 1
    for i in range(1, 10):
        c[i] += c[i - 1]
    for i in range(len(a) - 1, -1, -1):
        digit = (a[i] // div) % 10
        b[c[digit] - 1] = a[i]
        c[digit] -= 1
    return b


def counting_sort_on_word(a, alpha_pos):
    c = dict.fromkeys(string.ascii_uppercase, 0)
    b = a[:]
    for word in a:
        c[word[alpha_pos]] += 1
    c_keys = sorted(c.keys())  # ["a", "b", "c" ...]
    for i in range(1, len(c)):
        c[c_keys[i]] += c[c_keys[i - 1]]
    """
    if we loop in order: the result word will be inverse but not the first letter
    ex: right result: ['BAR', 'BIG', 'BOX', 'COW', 'DIG', 'DOG']
        loop in order result ['BOX', 'BIG', 'BAR', 'COW', 'DOG', 'DIG']
    for word in a:
        b[c[word[alpha_pos]] - 1] = word
        c[word[alpha_pos]] -= 1
    """
    for i in range(len(a) - 1, -1, -1):
        b[c[a[i][alpha_pos]] - 1] = a[i]
        c[a[i][alpha_pos]] -= 1
    return b


def to_upper(a):
    l = []
    for i in a:
        l.append(i.upper())
    return l


print(radix_sort_on_digit(tests[0]["input"], tests[0]["digit"]))
print(radix_sort_on_word(tests[1]["input"], tests[1]["digit"]))
