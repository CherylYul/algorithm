# General Problem: Alice has some cards with numbers written on them.
# She arranges the cards in decreasing order, and lay them out face out in a sequence on a table.
# She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
# Write a function to help Bob locate the card

test = []
# case 1: target number in cards, return its position
test.append({"input": [90, 87, 65, 22, -3, -9, -44], "target": -9, "output": 5})
# case 2: target number not in cards, return -1
test.append({"input": [90, 87, 65, 22, -3, -9, -44], "target": 2, "output": -1})
# case 3: cards have multiple target number, return its smallest position
test.append({"input": [90, 87, -9, -9, -9, -9, -44], "target": -9, "output": 2})
# case 4: no cards, return -1
test.append({"input": [], "target": 2, "output": -1})


def linear_locate(a, target):
    if len(a) == 0:
        return -1
    pos = 0
    while pos < len(a):
        if a[pos] == target:
            return pos
        pos += 1
    return -1


# O(N)


def binary_locate(a, target):
    s, e = 0, len(a) - 1
    while s <= e:
        pos = (s + e) // 2
        if a[pos] == target:
            if pos > 0 and a[pos] == a[pos - 1]:
                e = pos - 1
            else:
                return pos
        elif a[pos] < target:
            e = pos - 1
        else:
            s = pos + 1
    return -1


# O(logN)

for t in test:
    print(linear_locate(t["input"], t["target"]) == t["output"])
    print(binary_locate(t["input"], t["target"]) == t["output"])
