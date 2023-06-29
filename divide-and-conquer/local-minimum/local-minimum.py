import numpy as np

test = []

# test 1: when local minimum at the corner of 3D plane, odd matrix 5
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
# test 2: when local minimum at the side of the 3D plane, odd matrix 5
test.append(
    {
        "input": [
            [3, 9, 4, 2, 1],
            [0, 1, 2, 6, 7],
            [5, 9, 10, 7, 4],
            [1, 5, 6, 12, 2],
            [2, 3, 4, 5, 6],
        ],
        "output": 0,
    }
)

# test 3: when local minimum at the side of the 3D plane, odd matrix 5
test.append(
    {
        "input": [
            [3, 9, 4, 2, 1],
            [0, 2, 2, 7, 7],
            [5, 9, 10, 7, 4],
            [1, 5, 6, 12, 2],
            [2, 3, 4, 5, 6],
        ],
        "output": 0,
    }
)

# test 4: when local minimum at the middle of matrix, odd matrix 5
test.append(
    {
        "input": [
            [3, 9, 4, 2, 1],
            [0, 2, 2, 7, 7],
            [5, 9, 0, 7, 4],
            [1, 5, 6, 12, 2],
            [2, 3, 4, 5, 6],
        ],
        "output": 0,
    }
)

# test 5: when local minimum is next cell value, odd matrix 11
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
            [45, 64, 21, 20, 1, 59, 1, 23, 44, 55, 66],
        ],
        "output": 1,
    }
)

# test 6: even matrix 6
test.append(
    {
        "input": [
            [3, 9, 1, 2, 11, 6],
            [0, 1, 16, 6, 7, 9],
            [5, 9, 10, 7, 4, 12],
            [3, 5, 6, 12, 12, 14],
            [2, 3, 4, 5, 6, 15],
            [2, 3, 4, 5, 6, 15],
        ],
        "output": 0,
    }
)


def local_minimum(matrix, next_cell=None, next_cell_row=None, next_cell_col=None):
    # handle base case 1: matrix has no element
    if len(matrix) == 0:
        print("base case 1: ", matrix)
        return None

    # handle base case 2: matrix has 1 element
    if len(matrix) == 1:
        print("base case 2: ", matrix, matrix[0][0])
        return matrix[0][0]

    # handle base case 3: matrix 2x2 has 4 elements
    if len(matrix) == 2:
        print("base case 3: ", matrix)
        smallest_num, _ = find_smallest(
            [matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]]
        )
        return smallest_num

    # find smallest element in the middle row and middle column
    mid = len(matrix) // 2
    smallest_row, pos_col = find_smallest(matrix[mid])
    smallest_col, pos_row = find_smallest(np.array(matrix).T[mid])
    print("find middle element: ", smallest_row, smallest_col, pos_col, pos_row)
    if smallest_row <= smallest_col:
        middle_cell, middle_row, middle_col = smallest_row, mid, pos_col
    else:
        middle_cell, middle_row, middle_col = smallest_col, pos_row, mid

    # when local minimum at the middle of matrix
    if middle_row == mid and middle_col == mid:
        return middle_cell

    # if next_cell smaller than middle_cell, directly roll into the quadrant that has next_cell
    if next_cell and next_cell <= middle_cell:
        print("next cell 1: ", next_cell)
    # if middle_cell smaller than next_cell, find the next_cell and search for the quadrant to roll
    else:
        next_cell, next_cell_row, next_cell_col = get_next_cell(
            matrix, middle_row, middle_col
        )
        print("next cell 2: ", next_cell)
        # when local minimum at the middle_cell value, we don't need to roll
        if next_cell_row == middle_row and next_cell_col == middle_col:
            return next_cell
        # if not search for the quadrant to roll
    return search_quadrant(matrix, next_cell, next_cell_row, next_cell_col)


def find_smallest(a):
    smallest_num, pos = a[0], 0
    for i in range(1, len(a)):
        if a[i] < smallest_num:
            smallest_num, pos = a[i], i
    return smallest_num, pos


def search_quadrant(matrix, next_cell, next_cell_row, next_cell_col):
    mid = len(matrix) // 2
    if next_cell_row < mid:
        if next_cell_col < mid:
            print("search top-left")
            return local_minimum(
                [matrix[i][:mid] for i in range(0, mid)],
                next_cell,
                next_cell_row,
                next_cell_col,
            )  # top-left
        else:
            print("search top-right")
            return local_minimum(
                [matrix[i][mid + 1 :] for i in range(0, mid)],
                next_cell,
                next_cell_row,
                next_cell_col,
            )  # top-right
    else:
        if next_cell_col < mid:
            print("search bottom-left")
            return local_minimum(
                [matrix[i][:mid] for i in range(mid + 1, len(matrix))],
                next_cell,
                next_cell_row,
                next_cell_col,
            )  # bottom-left
        else:
            print("search bottom-right")
            return local_minimum(
                [matrix[i][mid + 1 :] for i in range(mid + 1, len(matrix))],
                next_cell,
                next_cell_row,
                next_cell_col,
            )  # bottom-right


def get_next_cell(matrix, middle_row, middle_col):
    mid = matrix[middle_row][middle_col]

    if middle_row == (len(matrix) // 2):
        top = matrix[middle_row - 1][middle_col]
        bottom = matrix[middle_row + 1][middle_col]
        if top <= mid and top <= bottom:
            return top, middle_row - 1, middle_col
        if bottom < mid and bottom < top:
            return bottom, middle_row + 1, middle_col

    if middle_col == (len(matrix) // 2):
        left = matrix[middle_row][middle_col - 1]
        right = matrix[middle_row][middle_col + 1]
        if left <= mid and left <= right:
            return left, middle_row, middle_col - 1
        if right < mid and right < left:
            return bottom, middle_row, middle_col + 1

    return mid, middle_row, middle_col


for i in range(len(test)):
    print(local_minimum(test[i]["input"]) == test[i]["output"])
