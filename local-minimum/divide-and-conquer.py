import numpy as np

test = []
test.append(
    {
        "input": [
            [30, 100, 20, 19, 18],
            [29, 101, 21, 104, 17],
            [28, 102, 22, 105, 16],
            [27, 103, 23, 106, 15],
            [26, 25, 24, 107, 14],
        ],
        "output": 14,
    }
)
test.append(
    {
        "input": [
            [3, 9, 4, 2, 1],
            [0, 1, 2, 6, 7],
            [5, 9, 10, 7, 4],
            [1, 5, 6, 12, 2],
            [2, 3, 4, 5, 6],
        ],
        "output": 1,
    }
)

test.append(
    {
        "input": [
            [23, 22, 39, 26, 25, 50, 20, 74, 28, 94, 100],
            [20, 19, 18, 62, 27, 49, 21, 22, 23, 24, 25],
            [37, 39, 33, 34, 35, 48, 49, 50, 51, 23, 22],
            [13, 15, 32, 12, 1, 10, 11, 12, 13, 14, 150],
            [24, 3, 31, 5, 61, 47, 82, 28, 92, 33, 11],
            [46, 45, 30, 44, 43, 60, 51, 52, 53, 54, 55],
            [23, 43, 2, 55, 57, 56, 18, 29, 93, 44, 55],
            [54, 23, 12, 15, 16, 57, 65, 43, 32, 21, 10],
            [23, 34, 45, 56, 67, 58, 99, 11, 22, 33, 44],
            [45, 64, 21, 20, 1, 59, 1, 23, 44, 55, 66, 99],
        ],
        "output": 1,
    }
)


def local_minimum(a, next_cell=None, next_cell_row=None, next_cell_col=None):
    # handle base case: 2x2 matrix
    if len(a) <= 2:
        return smallest_matrix_22(a, next_cell)

    # find smallest element in the middle row and middle column
    mid = len(a) // 2
    middle, middle_row, middle_col = middle_smallest(a)

    # roll into the quadrant that has next_cell
    if next_cell:
        if next_cell < middle:
            search_quadrant(a, next_cell, next_cell_row, next_cell_col)

    # when local minimum at the middle of matrix
    if middle == a[mid][mid]:
        return a[mid][mid]

    # search for the right quadrant to roll
    next_cell, next_cell_row, next_cell_col = get_next_cell(a, middle_row, middle_col)

    if next_cell_row < mid:
        if next_cell_col < mid:
            local_minimum(
                a[:mid][:mid], next_cell, next_cell_row, next_cell_col
            )  # top-left
        else:
            local_minimum(
                a[:mid][mid:], next_cell, next_cell_row, next_cell_col
            )  # top-right
    else:
        if next_cell_col < mid:
            local_minimum(
                a[mid:][:mid], next_cell, next_cell_row, next_cell_col
            )  # bottom-left
        else:
            local_minimum(
                a[mid:][mid:], next_cell, next_cell_row, next_cell_col
            )  # bottom-right


def smallest_matrix_22(a, next_cell):
    pass


def middle_smallest(a):
    pass


def search_quadrant():
    pass


def get_next_cell(a, middle_row, middle_col):
    mid = a[middle_row, middle_col]

    if middle_row == (len(a) // 2):
        top = a[middle_row - 1][middle_col]
        bottom = a[middle_row + 1][middle_col]
        if top < mid and top < bottom:
            return top, middle_row - 1, middle_col
        if bottom < mid and bottom < top:
            return bottom, middle_row + 1, middle_col

    if middle_col == (len(a) // 2):
        left = a[middle_row][middle_col - 1]
        right = a[middle_row][middle_col + 1]
        if left < mid and left < right:
            return left, middle_row, middle_col - 1
        if right < mid and right < top:
            return bottom, middle_row, middle_col + 1

    return mid, middle_row, middle_col


def smallest_3_elements(a, mid, b):
    if a < mid and a < b:
        return a
    if b < mid and b < a:
        return b
    return mid


a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.T[1])
