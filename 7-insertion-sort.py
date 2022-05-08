# General problem: sorting problem

tests = []
# Case 1: sorting array
tests.append({"input": [2, 4, 5, 6, 7, 9], "output": [2, 4, 5, 6, 7, 9]})
# Case 2: random array
tests.append({"input": [8, 4, 2, 6, 7, 1], "output": [1, 2, 4, 6, 7, 8]})
# Case 3: descending array
tests.append({"input": [9, 7, 6, 5, 4, 2], "output": [2, 4, 5, 6, 7, 9]})


def insertion_sort(array):
    for i in range(1, len(array)):
        # Create the temp to store the removing value of the index
        temp = array[i]
        # Keep compare the stored value with the previous number, if the previous is larger
        # we move to the next position and continue compare the previous one until reach the first element
        # If the previous one is smaller we stop immediately
        position = i - 1
        while position >= 0:
            if array[position] > temp:
                array[position + 1] = array[position]
                position -= 1
            else:
                break
        # Adding the stored value to its right position
        array[position + 1] = temp
    return array


for i, v in enumerate(tests):
    print(insertion_sort(v["input"]) == v["output"])

# Complexity Analysis: in the worst case scenario, insertion sort takes 1 + 2 + ... + (N-1) comparisons which is N^2/2
# then moving the position 1 + 2 + ... + (N-1) which is N^2/2, remove is N-1 times and insert is N-1 times
# Then we need total N^2 + 2N - 2 steps => Big O: O(N^2)
# Insertion sort is not efficiency as selection sort actually in the worst case
# But in the best case it only takes N steps in comparison than do nothing with moving, insert & remove
