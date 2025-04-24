import numpy as np
import math
import time

test = []

test.append(
    {
        "matrixA": np.array([[2, 3], [4, 5]]),
        "matrixB": np.array([[0, 2], [7, 1]]),
        "output": np.array([[21, 7], [35, 13]]),
    }
)

test.append(
    {
        "matrixA": np.array([[1, 3], [7, 5]]),
        "matrixB": np.array([[6, 8], [4, 2]]),
        "output": np.array([[18, 14], [62, 66]]),
    }
)

test.append(
    {
        "matrixA": np.array([[1, 2, 3], [3, 2, 1], [1, 2, 3]]),
        "matrixB": np.array([[4, 5, 6], [6, 5, 4], [4, 6, 5]]),
        "output": np.array([[28, 33, 29], [28, 31, 31], [28, 33, 29]]),
    }
)

test.append(
    {
        "matrixA": np.array([[1, 2, 3, 1], [3, 2, 1, 0], [1, 2, 2, 3], [1, 2, 0, -1]]),
        "matrixB": np.array([[4, 2, 3, 6], [-1, 6, 5, 4], [0, 4, 6, 5], [-1, 2, 4, 5]]),
        "output": np.array(
            [[1, 28, 35, 34], [10, 22, 25, 31], [-1, 28, 37, 39], [3, 12, 9, 9]]
        ),
    }
)


def matrix_multiplication_brute_force(A, B):
    C = np.zeros(A.shape)
    for i in range(len(C)):
        for j in range(len(C)):
            for k in range(len(C)):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]
    return C


def check_matrix_length(A):
    size = len(A)
    if size == 1 or size == 2:
        return A
    for i in range(2, 20):
        strassen_size = math.pow(2, i)
        if size == strassen_size:
            return A
        elif size < strassen_size:
            new_A = np.zeros((strassen_size, strassen_size))
            new_A[:size, :size] = A
            break
    return new_A


def matrix_multiplication_strassen(A, B, matrix_length=False):
    if matrix_length == False:
        A = check_matrix_length(A)
        B = check_matrix_length(B)
        matrix_length = True

    # handle base case
    if len(A) == 1:
        # print("base case: ", A[0][0] * B[0][0])
        return A[0][0] * B[0][0]

    C = np.zeros(A.shape)
    mid = len(C) // 2

    # print("calculate A and B: ")
    A11 = A[:mid, :mid]
    A12 = A[:mid, mid:]
    A21 = A[mid:, :mid]
    A22 = A[mid:, mid:]
    B11 = B[:mid, :mid]
    B12 = B[:mid, mid:]
    B21 = B[mid:, :mid]
    B22 = B[mid:, mid:]
    # print(A11, A12, A21, A22, B11, B12, B21, B22)

    # calculate the sum matrices
    # print("calculate the sum matrices: ")
    S1 = B12 - B22
    S2 = A11 + A12
    S3 = A21 + A22
    S4 = B21 - B11
    S5 = A11 + A22
    S6 = B11 + B22
    S7 = A12 - A22
    S8 = B21 + B22
    S9 = A11 - A21
    S10 = B11 + B12
    # print(S1, S2, S3, S4, S5, S6, S7, S8, S9, S10)

    # calculate the product matrices
    # print("calculate the product matrices: ")
    P1 = matrix_multiplication_strassen(A11, S1, matrix_length)
    P2 = matrix_multiplication_strassen(S2, B22, matrix_length)
    P3 = matrix_multiplication_strassen(S3, B11, matrix_length)
    P4 = matrix_multiplication_strassen(A22, S4, matrix_length)
    P5 = matrix_multiplication_strassen(S5, S6, matrix_length)
    P6 = matrix_multiplication_strassen(S7, S8, matrix_length)
    P7 = matrix_multiplication_strassen(S9, S10, matrix_length)
    # print(P1, P2, P3, P4, P5, P6, P7)

    C[:mid, :mid] = P5 + P4 - P2 + P6
    C[:mid, mid:] = P1 + P2
    C[mid:, :mid] = P3 + P4
    C[mid:, mid:] = P5 + P1 - P3 - P7

    return C


for i, t in enumerate(test):

    start = time.time()
    print(matrix_multiplication_brute_force(t["matrixA"], t["matrixB"]))
    bf_time = time.time() - start

    start = time.time()
    print(matrix_multiplication_strassen(t["matrixA"], t["matrixB"]))
    ss_time = time.time() - start

    print(bf_time, " vs ", ss_time)
