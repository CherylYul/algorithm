# find the maximum element in unimodal array (no repeated elements)
# unimodal array is one that has a sequence increasing integers
# followed by a sequence of decreasing integers

test = []
# case 1: maximum element at the middle
test.append({"input": [2, 3, 5, 31, 42, 59, 38, 18, 11, 9, 6, 1], "output": 59})
# case 2: maximum element not in the middle, but in the right
test.append({"input": [7, 8, 22, 36, 45, 89, 77], "output": 89})
# case 3: maximum element not in the middle, but in the left
test.append({"input": [65, 93, 100, 76, 25, 13, 6, -3, -28, -45], "output": 100})
# case 4: no cards, return -1
test.append({"input": [], "output": -1})


def find_max_in_unimodal(a):
    start, end = 0, len(a) - 1
    while start <= end:
        max_pos = (start + end) // 2
        if a[max_pos] > a[max_pos + 1] and a[max_pos] > a[max_pos - 1]:
            return a[max_pos]
        elif a[max_pos] < a[max_pos + 1]:
            start = max_pos + 1
        elif a[max_pos] < a[max_pos - 1]:
            end = max_pos - 1
    return -1


for t in test:
    print(find_max_in_unimodal(t["input"]) == t["output"])
