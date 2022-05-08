# General problem: same problem in sorting which we have to sort a list in ascending way

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


def selection_sort(array):
    # Iterate the variables in the list
    for i in range(len(array) - 1):
        # With each pass-through, compare the current position with after value in the list, find the lowest number
        lowest_num = i
        for j in range(i + 1, len(array)):
            if array[lowest_num] > array[j]:
                lowest_num = j
        # Swap the value 
        array[i], array[lowest_num] = array[lowest_num], array[i]
    return array


for i, v in enumerate(tests):
    print(selection_sort(v["input"]) == v["output"])

# Complexity Analysis: the selection sort look seem like bubble sort which has 2 loops.
# Actually, when we break it down in N array, we need to compare (N-1) + (N-2) + ... + 1 times + N-1 swap step
# For example, with 5 elements bubble sort takes 20 steps (~N^2) 4*2 + 3*2 + 2*2 + 2*1 = 20
# selection sort takes 14 steps (~(N^2)/2) 4 + 3 + 2 + 1 + 4 = 14 which faster than double times, but Big O still O(N) = N^2

