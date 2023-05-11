a = [1, 3, 5, 2, 4, 6]


def brute_force(a):
    count = 0
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                count += 1
    return count


print(brute_force(a))
