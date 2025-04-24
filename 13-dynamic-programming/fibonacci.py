"""
Fibonacci number: F(n) = F(n-1) + F(n-2)
Sequence: 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
Applications: petals on flowers, human body...
"""


def Fibonacci_dp(n):
    F = [0 for _ in range(n + 1)]
    F[1] = 1
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]


def Fibonacci_memoize(n):
    F = [0 for _ in range(n + 1)]
    F[1] = 1

    def Fibonacci(n):
        if n == 0:
            return 0
        if F[n]:
            return F[n]
        return Fibonacci(n - 1) + Fibonacci(n - 2)

    return Fibonacci(n)


print(Fibonacci_dp(10))
print(Fibonacci_memoize(10))
# python3 dynamic-programming/fibonacci.py
