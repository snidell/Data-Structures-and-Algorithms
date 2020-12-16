# Given a boolean matrix, update it so that if any cell is true, all the
# cells in that row and column are true.
# Are we returning a new array or modifiying in place? --> modifiy in place
# https://www.byte-by-byte.com/zeromatrix/?utm_source=optin_carrot&utm_medium=pdf&utm_campaign=50questions


def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()


def zero_matrix(matrix):
    # if we dont have a matric get out
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return
    rowZero = False
    colZero = False
    # is the first row true?
    for j in range(len(matrix[0])):
        rowZero |= matrix[0][j]

    # first column true?
    for i in range(len(matrix)):
        colZero |= matrix[i][0]

    # proceed through the rest of the matrix
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if(matrix[i][j]):
                # set row ot be True
                matrix[i][0] = True
                # set column to be True
                matrix[0][j] = True

    # loop through first column and set each row to be true where cell in
    # first column is True
    for i in range(1, len(matrix)):
        if matrix[i][0]:
            for j in range(1, len(matrix)):
                matrix[i][j] = True

    # loop through first row and set each col to be true where cell in first
    # row is True
    for j in range(1, len(matrix[0])):
        if matrix[0][j]:
            for i in range(1, len(matrix)):
                matrix[i][j] = True
    # set for row to true if needed
    if rowZero:
        for j in range(len(matrix)):
            matrix[0][j] = True
    if colZero:
        for i in range(len(matrix)):
            matrix[i][0] = True
    printMatrix(matrix)
    return matrix


def main():

    array1 = [
        [True, False, False],
        [False, False, False],
        [False, False, False]
    ]
    zero_matrix(array1)

    array2 = [
        [True, False, False],
        [False, False, False],
        [False, False, False]
    ]

    zero_matrix(array2)
    print("")
    array3 = [
        [False, False, False],
        [True, False, False],
        [False, False, False]
    ]

    zero_matrix(array3)


if __name__ == "__main__":
    main()
