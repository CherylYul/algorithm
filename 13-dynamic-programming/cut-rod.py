"""
Enterprise buys long steel rods and cut them into shorter rods, each rods'
length sells different price. Find the best way to cut the rods.
"""

rods = {
    "length": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "price": [0, 1, 5, 6, 9, 10, 17, 17, 20, 24, 30],
}


# O(n^2) ~ DFS
def cut_rod_memoized(n, price_list):
    a = [-float("inf") for _ in range(n + 1)]

    def internal_memoized(n, a, price_list):
        if a[n] >= 0:
            return a[n]
        if n == 0:
            return 0
        optimize = -float("inf")
        for i in range(1, n + 1):
            optimize = max(
                optimize, price_list[i] + internal_memoized(n - i, a, price_list)
            )
        a[n] = optimize
        return optimize

    return internal_memoized(n, a, price_list)


# O(n^2) ~ topological sort
def cut_rod_dp(n, price_list):
    a = [-float("inf") for _ in range(n + 1)]
    a[0] = 0
    for j in range(1, n + 1):
        optimize = -float("inf")
        for i in range(1, j + 1):
            optimize = max(optimize, price_list[i] + a[j - i])
        a[j] = optimize
    return a[n]


def extend_bottom_up(n, price_list):
    s = [None for _ in range(n + 1)]
    a = [None for _ in range(n + 1)]
    a[0] = 0
    for j in range(1, n + 1):
        optimize = -float("inf")
        for i in range(1, j + 1):
            if optimize < price_list[i] + a[j - i]:
                optimize = price_list[i] + a[j - i]
                s[j] = i
        a[j] = optimize
    return s, a


def print_solution(n, price_list):
    s, a = extend_bottom_up(n, price_list)
    str = ""
    for i in range(n + 1):
        str += "{}: {}, {} \n".format(i, a[i], s[i])
    return str


print(cut_rod_memoized(4, rods["price"]))
print(cut_rod_dp(4, rods["price"]))
print(print_solution(10, rods["price"]))

# python3 dynamic-programming/cut-rod.py
