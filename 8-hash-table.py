# Problem 1: Find the same hobbies between users with Big O: O(N)
from sqlalchemy import true

tests = []
tests.append(
    {
        "input": {
            "u1": ["machine learning", "cryptography", "swimming", "stock", "reading"],
            "u2": [
                "cooking",
                "data science",
                "research",
                "swimming",
                "stock",
                "film",
                "machine learning",
            ],
        },
        "output": ["machine learning", "swimming", "stock"],
    }
)


def same_hobbie(a1, a2):
    d = {}
    hobbie = []
    if len(a1) > len(a2):
        long = a1
        short = a2
    else:
        long = a2
        short = a1
    for i, v in enumerate(long):
        d[v] = true
    for i, v in enumerate(short):
        try:
            if d[v]:
                hobbie.append(v)
        except KeyError:
            continue
    return hobbie


print(
    same_hobbie(tests[0]["input"]["u1"], tests[0]["input"]["u2"]) == tests[0]["output"]
)

# Problem 2: Missing letter of alphabet
case = "the quick brown box jumps over a lazy dog"
alphabet = "abcdefghijklmnopqrstuvwxyz "


def missing_letter(alpha, target):
    d, m = {}, []
    i = 0
    while i < len(alpha):
        curr = alpha[i]
        d[curr] = 0
        i += 1
    i = 0
    while i < len(case):
        curr = case[i]
        d[curr] += 1
        i += 1
    i = 0
    for i in d:
        if d[i] == 0:
            m.append(i)
    return m


print(missing_letter(alphabet, case))
