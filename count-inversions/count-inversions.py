test = []

test.append(
    {
        "input": [2, 3, 8, 6, 1],
        "output": 5,
        "detailed-pairs": [(1, 5), (2, 5), (3, 4), (3, 5), (4, 5)],
    }
)

test.append(
    {
        "input": [1, 3, 5, 2, 4, 6],
        "output": 3,
        "detailed-pairs": [(2, 4), (3, 4), (3, 5)],
    }
)

test.append(
    {
        "input": [6, 5, 4, 3, 2, 1],
        "output": 15,
        "detailed-pairs": [
            (1, 2),
            (1, 3),
            (1, 4),
            (1, 5),
            (1, 6),
            (2, 3),
            (2, 4),
            (2, 5),
            (2, 6),
            (3, 4),
            (3, 5),
            (3, 6),
            (4, 5),
            (4, 6),
            (5, 6),
        ],
    }
)


def count_inversions_brute_force(a):
    count = 0
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                count += 1
    return count


def count_inversions(a):
    if len(a) == 1:
        return a, 0
    mid = len(a) // 2

    # print("count left inversions: ", a[:mid])
    left, left_inv = count_inversions(a[:mid])
    # print("left inversions is: ", left_inv)
    # print("left is: ", left)

    # print("count right inversions: ", a[mid:])
    right, right_inv = count_inversions(a[mid:])
    # print("right inversions is: ", right_inv)
    # print("right is: ", right)

    new_a, inv = merge(left, right)
    total_inv = inv + left_inv + right_inv
    return new_a, total_inv


def merge(left_a, right_a):
    i, j, a = 0, 0, []
    inv = 0
    # print("start merge! ", left_a, right_a)
    while i < len(left_a) and j < len(right_a):
        if right_a[j] < left_a[i]:
            a.append(right_a[j])
            inv = inv + len(left_a) - i
            j += 1
        else:
            a.append(left_a[i])
            i += 1
    # print("finish merge: ", inv)
    # print("finish merge: ", a + left_a[i:] + right_a[j:])
    return a + left_a[i:] + right_a[j:], inv


print(count_inversions(test[2]["input"]))
