# karatsuba multiplication algorithm
def rectIntMult(x, y):
    if x < 10 or y < 10:
        return x * y
    n = min(digit_nums(x), digit_nums(y))
    # this line of code permits different length of n
    # n = check_digit_length(max(digit_nums(x), digit_nums(y)))
    p = pow(10, n / 2)
    a = x / p
    b = x % p
    c = y // p
    d = y % p
    # print("a: ", a, ", b: ", b, ", c: ", c, ", d: ", d)
    ac = rectIntMult(a, c)
    bd = rectIntMult(b, d)
    ad_bc = rectIntMult(a + b, c + d) - ac - bd
    # print("ac: ", ac, " bd: ", bd, " ad_bc: ", ad_bc)
    return pow(10, n) * ac + p * ad_bc + bd


def digit_nums(n):
    if n == 0:
        return 0
    return 1 + digit_nums(n / 10)


def check_digit_length(n):
    i = 0
    while True:
        if pow(2, i) < n:
            i += 1
        else:
            return pow(2, i)


y = 1234
x = 5678
print(rectIntMult(x, y))
