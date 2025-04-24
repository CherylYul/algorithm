# adding 2 n-bit binary stored in 2 n-element arrays A and B to
# (n+1) binary element store in array C


test = []

test.append(
    {
        "input1": [1, 0, 0, 0, 1, 0],
        "input2": [1, 1, 0, 0, 0, 1],
        "output": [1, 0, 1, 0, 0, 1, 1],
    }
)

test.append(
    {
        "input1": [0, 1, 0, 1, 0, 1],
        "input2": [1, 0, 1, 0, 0, 1],
        "output": [1, 1, 1, 1, 1, 0],
    }
)

test.append(
    {
        "input1": [1, 1, 1],
        "input2": [1, 1, 1],
        "output": [1, 1, 1, 0],
    }
)


def adding_binary(A, B):
    C = [0 for i in range(len(A) + 1)]
    pos = len(C) - 1
    memo = False
    while pos > 0:
        if memo:
            C[pos] = 1
            memo = False
        C[pos] = C[pos] + A[pos - 1] + B[pos - 1]
        if C[pos] == 2:
            C[pos] = 0
            memo = True
        if C[pos] == 3:
            C[pos] = 1
            memo = True
        pos -= 1
    C[pos] = 1 if memo else 0
    return C


print(adding_binary(test[2]["input1"], test[2]["input2"]))
