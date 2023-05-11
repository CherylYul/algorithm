test1 = [1, 3, 5, 2, 4, 6]
test2 = [6, 5, 4, 3, 2, 1]


def sort_and_count_inv(a, count=0):
    if len(a) <= 1:
        return a
    mid = len(a) / 2
    left_inv = sort_and_count_inv(a[:mid], count)
    right_inv = sort_and_count_inv(a[mid:], count)
    return merge_and_count_split_inv(left_inv, right_inv, count)


def merge_and_count_split_inv(a1, a2, count):
    i, j, a = 0, 0, []
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            a.append(a1[i])
            i += 1
        else:
            a.append(a2[j])
            j += 1
            count = count + len(a2) / 2 - i + 1
            print(count)
    return a + a1[i:] + a2[j:]


print(sort_and_count_inv(test1))
print(sort_and_count_inv(test2))
