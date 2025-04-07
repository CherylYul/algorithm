# error in case 11, 19, 17 which should return 1 but it returns 0
def solution(A, B, K):
    dif = B - A
    num = 0
    if (A % K == 0) or (B % K == 0):
        num = 1
    if dif < K:
        return num
    return num + dif // K


# chan tren chan duoi lai
# O(1)
def solution(A, B, K):
    dif = B - A
    if dif < K:
        for i in range(A, B + 1):
            if i % K == 0:
                return 1
    # (11 // 17 + 1) * 17 = 17
    # (345 // 17) * 17 = 340
    start = A if (A % K == 0) else (A // K + 1) * K
    end = B if (B % K == 0) else (B // K) * K
    if start == end:
        return 1
    return (end - start) // K + 1
