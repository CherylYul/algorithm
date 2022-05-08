# General problems: we have the tasks that need to sort the rating list of our products

tests = []
# Case 1: the rating already sorted
tests.append(
    {
        "input": [2.4, 3.5, 5.5, 6.7, 7.7, 8.7, 9.0, 9.1],
        "output": [2.4, 3.5, 5.5, 6.7, 7.7, 8.7, 9.0, 9.1],
    }
)
# Case 2: the rating is randomly
tests.append(
    {
        "input": [6.9, 3.5, 5.5, 4.0, 4.1, 4.2, 6.3, 7.1],
        "output": [3.5, 4.0, 4.1, 4.2, 5.5, 6.3, 6.9, 7.1],
    }
)
# Case 3: the rating is in decreasing order also repeating list
tests.append(
    {
        "input": [9.9, 9.8, 9.4, 9.4, 9.4, 9.2, 9.1, 9.0, 8.9, 8.8, 8.8, 8.7],
        "output": [8.7, 8.8, 8.8, 8.9, 9.0, 9.1, 9.2, 9.4, 9.4, 9.4, 9.8, 9.9],
    }
)


def bubble_sort(array):
    # Create variable keep track of the rightmost index of the array that has not yet been sorted
    length = len(array) - 1
    sorted = False
    while not sorted:
        sorted = True
        # If the list has not been sorted, continue compare each number with the number follow it
        # If number is greatet than the one follows, swap them, continue do it until the list sorted
        for i in range(length):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
        length -= 1
    return array


for i, v in enumerate(tests):
    print(bubble_sort(v["input"]) == v["output"])

# Complexity Analysis: we can see that in the worst case our list will in the descending order
# With N elements, we have to compare and swap 2(N-1) + 2(N-2) + 2(N-3) + ... + 2 which is almost equal N*N times
# Therefore, using bubble sort, we will encounter quadratic problems - Big O = O(N^2)
