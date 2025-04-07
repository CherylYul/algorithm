# Find the same hobbies between users with Big O: O(N)
tests = []
tests.append(
    {
        "u1": ["machine learning", "cryptography", "swimming", "stock", "reading"],
        "u2": ["stock", "research", "swimming", "machine learning"],
        "same": ["stock", "swimming", "machine learning"],
    }
)

tests.append(
    {
        "u1": ["music", "cryptography", "swimming", "stock", "reading"],
        "u2": ["research", "swimming", "film", "marketing", "reading", "sing"],
        "same": ["swimming", "reading"],
    }
)


def same_hobbie(a1, a2):
    d, hobbie = {}, []
    if len(a1) > len(a2):
        long, short = a1, a2
    else:
        long, short = a2, a1
    for i in long:
        d[i] = True
    for i in short:
        try:
            if d[i]:
                hobbie.append(i)
        except KeyError:
            continue
    return hobbie


print(same_hobbie(tests[0]["u1"], tests[0]["u2"]) == tests[0]["same"])
print(same_hobbie(tests[1]["u1"], tests[1]["u2"]) == tests[1]["same"])
