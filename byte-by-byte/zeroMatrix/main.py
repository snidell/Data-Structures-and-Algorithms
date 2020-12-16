
def zero_matrix(matrix):

    # if we dont have a matrix return
    if len(matrix) < 1 or len(matrix[0]) < 1:
        return
    rowZero = False
    colZero = False

    #is the first row have any True values?
    for j in range(len(matrix[0])):
        rowZero |= matrix[0][j]

    #is the first column have any True Values?
    for i in range(len(matrix)):
        colZero |= matrix[i][0]

    #now that we have the first row and column taken care of lets proceed with [1][1] index

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]:
                #set the corresponding column to True at index Zero
                matrix[i][0] = True
                # set the corresponding row to True at index Zero
                matrix[0][j] = True

    # fill in the rest of the matrix now that the first row and col reflect what needs to be filled in
    # column
    for i in range(1,len(matrix)):
        if matrix[i][0]:
            for j in range(1,len(matrix[0])):
                matrix[i][j] = True
    # row
    for j in range(1,len(matrix[0])):
        if matrix[0][j]:
            for i in range(1,len(matrix)):
                matrix[i][j] = True

    if rowZero:
        for j in range(len(matrix[0])):
            matrix[0][j] = True

    if colZero:
        for i in range(len(matrix)):
            matrix[i][0] = True

    print_matrix(matrix)
    print("")

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end ="")
        print("")


def main():
    array1 = [
        [True,False,False],
        [False,False,False],
        [False,False,False]
    ]
    zero_matrix(array1)
    array2 = [
        [False,False,False],
        [False,True,False],
        [False,False,True]
    ]
    zero_matrix(array2)
    array3 = [
        [True,False,False],
        [True,False,False],
        [False,False,False]
    ]
    zero_matrix(array3)

if __name__ == "__main__":
    main()
