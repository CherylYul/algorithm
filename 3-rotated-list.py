# Gernaral problem: Given a sorted list that was rotated some unknown number of times.
# We need to find the number of times it was rotated

tests = []
# Case 1: A list that was not rotated or rotated n times or an empty list, return 0
tests.append({"input": [4, 7, 18, 22, 24, 28, 32, 35, 66, 78, 92], "output": 0})
# Case 2: A list rotated just once or n-1 times or from 1 to n-1 times
tests.append({"input": [66, 78, 92, 4, 7, 18, 22, 24, 28, 32, 35], "output": 3})
tests.append({"input": [22, 24, 28, 32, 35, 66, 78, 92, 4, 7, 18], "output": 8})
# Case 3: A rotated list with multiple repeated number
tests.append(
    {"input": [34, 34, 34, 55, 62, 77, 77, 77, 89, 2, 4, 5, 5, 34], "output": 9}
)

# From test case we realize that if the middle element is smaller than the last element then the answer is in the first half
# If the middle element is bigger than the first element of the list then the answer is in the second half


def binary_search(array):
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


for i, v in enumerate(tests):
    print(binary_search(v["input"]) == v["output"])

# Complexity Analysis: base on the binary search algorithm => Big O = O(log N)
