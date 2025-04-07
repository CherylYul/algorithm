# fing the missing letter of alphabet
case = "the quick brown box jumps over a lazy dog"
alphabet = "abcdefghijklmnopqrstuvwxyz "


def missing_letter(alphabet, target):
    d, m, i1, i2 = {}, [], 0, 0
    while i1 < len(alphabet):
        curr = alphabet[i1]
        d[curr] = 0
        i1 += 1
    while i2 < len(case):
        curr = case[i2]
        d[curr] += 1
        i2 += 1
    for i in d:
        if d[i] == 0:
            m.append(i)
    return m


print(missing_letter(alphabet, case))
