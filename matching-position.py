# Problem: given sorted array from smallest to largest,
# decide whether or not there is an index i such that A[i] = i

test = []
# case 1: there is matching element in the list
test.append({"input": [-2, 0, 2, 33, 42, 59, 88, 89, 111, 9, 6, 1], "output": "yes"})
# case 2: there is not matching element in the list
test.append({"input": [-55, -34, -5, -3, 2, 7, 8, 22, 36, 45, 89, 100], "output": "no"})
# case 3: there is matching element in the list
test.append({"input": [-77, -48, -22, -16, -5, 0, 2, 7, 9], "output": "yes"})
# case 4: nothing in the list
test.append({"input": [], "output": "no"})


def matching_position(a):
    start, end = 0, len(a) - 1
    while start <= end:
        pos = (start + end) // 2
        if a[pos] == pos:
            return "yes"
        elif a[pos] > pos:
            end = pos - 1
        else:
            start = pos + 1
    return "no"


for t in test:
    print(matching_position(t["input"]))

# O(logn)
