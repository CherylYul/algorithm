import math
import random
import time

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


def find_maximum_subarray_brute_force(a):
    sum = -float("inf")
    for i in range(len(a) - 1):
        temp_sum = 0
        for j in range(i, len(a)):
            temp_sum += a[j]
            if temp_sum > sum:
                start, end, sum = i, j, temp_sum
    return (start, end, sum)


def find_maximum_subarray(a):
    start, end = 0, len(a)

    # handle base case
    if len(a) == 1:
        # print("base case: ", a)
        return start, end, a[start]

    # divide conquer combine
    mid = (start + end) // 2
    left_start, left_end, max_left = find_maximum_subarray(a[:mid])
    right_start, right_end, max_right = find_maximum_subarray(a[mid:])
    cross_start, cross_end, max_cross = find_max_crossing_subarray(a, start, mid, end)

    # compare and return the max value
    if max_left >= max_right and max_left >= max_cross:
        # print("the max on the left: ", max_left)
        return left_start, left_end, max_left
    elif max_right >= max_left and max_right >= max_cross:
        # print("the max on the right: ", max_right)
        return right_start, right_end, max_right
    else:
        # print("the max on the cross: ", max_cross)
        return cross_start, cross_end, max_cross


def find_max_crossing_subarray(a, start, mid, end):
    left_max, sum = -float("inf"), 0
    for l in range(mid - 1, start - 1, -1):
        sum += a[l]
        if sum > left_max:
            cross_start = l
            left_max = sum

    right_max, sum = -float("inf"), 0
    for r in range(mid, end):
        sum += a[r]
        if sum > right_max:
            cross_end = r
            right_max = sum

    # print("combine: ", left_max, right_max, left_max + right_max)
    return cross_start, cross_end, left_max + right_max


def find_maximum_subarray_linear(a):
    start, end, max_profit = 0, 0, 0
    profit = 0
    for i in range(len(a)):
        profit += a[i]
        if profit > max_profit:
            max_profit = profit
            end = i
        if profit < 0:
            start = i + 1
            profit = 0
    return start, end, max_profit


a = price_to_change(test[0]["input"])
print(find_maximum_subarray_brute_force(a))
print(find_maximum_subarray(a))
print(find_maximum_subarray_linear(a))
# buy at day 7 and sell at day 11


# compare running time among brute-force, divide and conquer, linear
NUM_ITERATIONS = 10
for input_size in range(2, 100):
    a = [random.randint(-100, 100) for _ in range(input_size)]

    start = time.time()
    for _ in range(NUM_ITERATIONS):
        bf = find_maximum_subarray_brute_force(a)
    bf_time = time.time() - start

    start = time.time()
    for _ in range(NUM_ITERATIONS):
        rc = find_maximum_subarray(a)
    rc_time = time.time() - start

    start = time.time()
    for _ in range(NUM_ITERATIONS):
        ln = find_maximum_subarray_linear(a)
    ln_time = time.time() - start

    print(input_size, " | ", bf_time, " | ", rc_time, " | ", ln_time)

    if bf_time > rc_time:
        print("Cross over point = ", input_size)
        break
