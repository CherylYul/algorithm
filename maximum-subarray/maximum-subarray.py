test = []

test.append(
    {
        "input": [
            100,
            113,
            110,
            85,
            105,
            102,
            86,
            63,
            81,
            101,
            94,
            106,
            101,
            79,
            94,
            90,
            97,
        ],
        "output": 43,
    }
)


def price_to_change(a):
    new_a = []
    for i in range(1, len(a)):
        new_a.append(a[i] - a[i - 1])
    return new_a


def find_maximum_subarray(a):
    start, end = 0, len(a)
    # handle base case
    if len(a) == 1:
        print("base case: ", a)
        return start, end, a[start]
    # divide and conquer
    mid = (start + end) // 2
    left_start, left_end, max_left = find_maximum_subarray(a[:mid])
    right_start, right_end, max_right = find_maximum_subarray(a[mid:])
    # combine
    cross_start, cross_end, max_cross = find_max_crossing_subarray(a, start, mid, end)
    # compare and return the max value
    if max_left >= max_right and max_left >= max_cross:
        print("the max on the left: ", max_left)
        return left_start, left_end, max_left
    elif max_right >= max_left and max_right >= max_cross:
        print("the max on the right: ", max_right)
        return right_start, right_end, max_right
    else:
        print("the max on the cross: ", max_cross)
        return cross_start, cross_end, max_cross


def find_max_crossing_subarray(a, start, mid, end):
    left_max, sum = -10000, 0
    for l in range(mid - 1, start - 1, -1):
        sum += a[l]
        if sum > left_max:
            cross_start = l
            left_max = sum
    right_max, sum = -10000, 0
    for r in range(mid, end):
        sum += a[r]
        if sum > right_max:
            cross_end = r
            right_max = sum
    print("combine: ", left_max, right_max, left_max + right_max)
    return cross_start, cross_end, left_max + right_max


a = price_to_change(test[0]["input"])
print(find_maximum_subarray(a))
