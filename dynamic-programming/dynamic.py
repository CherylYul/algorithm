rods = {
    "length": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "price": [0, 1, 5, 6, 9, 10, 17, 17, 20, 24, 30]
}

# O(n^2)
def cut_rod(n, value_list):
    if n == 0:
        return 0
    optimize = -float("inf")
    for i in range(1, n + 1):
        optimize = max(optimize, value_list[i] + cut_rod(n-i, value_list))
    return optimize


# O(n^2) ~ DFS
def memoized(n, value_list):
    a = [-float("inf") for _ in range(n+1)]
    return internal_memoized(n, a, value_list)


def internal_memoized(n, a, value_list):
    if a[n] >= 0:
        return a[n]
    if n == 0:
        return 0
    optimize = -float("inf")
    for i in range(1, n+1):
        optimize = max(optimize, value_list[i] + internal_memoized(n-i, a, value_list))
    a[n] = optimize
    return optimize


# O(n^2) ~ topological sort
def bottom_up(n, value_list):
    a = [-float("inf") for _ in range(n + 1)]
    a[0] = 0
    for j in range(1, n+1):
        optimize = -float("inf")
        for i in range(1, j+1):
            optimize = max(optimize, value_list[i] + a[j-i])
        a[j] = optimize
    return a[n]


def extend_bottom_up(n, value_list):
    s = [None for _ in range(n + 1)]
    a = [None for _ in range(n + 1)]
    a[0] = 0
    for j in range(1, n + 1):
        optimize = -float("inf")
        for i in range(1, j + 1):
            if optimize < value_list[i] + a[j - i]:
                optimize = value_list[i] + a[j-i]
                s[j] = i
        a[j] = optimize
    return s, a


def print_solution(n, value_list):
    s, a = extend_bottom_up(n, value_list)
    str = ""
    for i in range(n+1):
        str += "{}: {}, {} \n".format(i, a[i], s[i])
    return str


print(cut_rod(4, rods["price"]))
print(memoized(4, rods["price"]))
print(bottom_up(4, rods["price"]))
print(print_solution(10, rods["price"]))

#python3 dynamic-programming/dynamic.py