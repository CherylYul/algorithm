# Problem: You are given a rotating sorted list an unknown number of times.
# Write a function to determine the minimum number of times the original sorted list was rotated
# Your function should have the worst-case complexity of O(log N)

test = []
# Case 1: the list is rotated n times, the list is not rotated, return 0 rotating times
test.append({"input": [0, 4, 5, 6, 7, 8, 9], "output": 0})
# Case 2: the list is rotated k times which is k < n, return k
test.append({"input": [7, 8, 9, 0, 4, 5, 6], "output": 3})
# Case 3: the list is rotated k times which is k < n, have repeated number, return k
test.append({"input": [7, 8, 9, 7, 7, 7, 7], "output": 3})
# Case 4: the empty list, return 0
test.append({"input": [], "output": 0})


def number_of_rotate_times(array):
    # Create variable of the lowest point and the highest point
    lo, hi = 0, len(array) - 1
    while lo < hi:
        # Find the middle position
        mid = (lo + hi) // 2
        # If the middle point is smaller than the left one, return its position
        if array[mid] < array[mid - 1]:
            return mid
        # If the middle point is bigger than the next one, return its position adding by 1 value
        if array[mid] > array[mid + 1]:
            return mid + 1
        # if not then compare the middle point with the first and final element
        # if it is smaller than the final point means that the second half of the list is sorted
        # the position we want to find lie on the first half of the list, change the high boudary
        if array[mid] < array[hi] and array[mid] < array[lo]:
            hi = mid - 1
        # if it is bigger than the middle point means that the first half of the list is sorted
        # the seeking position is at the second half of the list, change the low boundary
        if array[mid] > array[lo] and array[mid] > array[hi]:
            lo = mid + 1
    return 0


for t in test:
    print(number_of_rotate_times(t["input"]) == t["output"])

# O(log N)
