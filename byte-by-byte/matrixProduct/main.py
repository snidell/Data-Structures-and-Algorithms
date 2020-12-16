#https://www.byte-by-byte.com/matrixproduct/?utm_source=optin_carrot&utm_medium=pdf&utm_campaign=50questions
#Question: Given a matrix, find the path from top left to bottom right with the greatest
#product by moving only down and right.
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
#
# 1 -> 4 -> 7 -> 8 -> 9

import sys
def maxProduct(matrix):
    #creating min and max cache for possible negative numbers
    maxCache = [[-sys.maxsize for x in range(len(matrix))]for x in range(len(matrix[0]))]
    minCache = [[sys.maxsize for x in range(len(matrix))]for x in range(len(matrix[0]))]


    #fill in cache from top left to bottom right
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            maxVal = -sys.maxsize
            minVal = sys.maxsize

            #if we are at the top corner just copy over.
            if i == 0 and j ==0:
                maxVal = matrix[i][j]
                minVal = matrix[i][j]
            #consider items to the check the rows above us to see if its better
            if i > 0:
                tempMax = max(matrix[i][j]*maxCache[i-1][j],matrix[i][j]*minCache[i-1][j])
                tempMin = min(matrix[i][j]*maxCache[i-1][j],matrix[i][j]*minCache[i-1][j])
                maxVal = max(tempMax,maxVal)
                minVal = min(tempMin,minVal)
            if j >0:
                tempMax = max(matrix[i][j]*maxCache[i][j-1] , matrix[i][j]*minCache[i][j-1])
                tempMin = min(matrix[i][j]*maxCache[i][j-1] , matrix[i][j]*minCache[i][j-1])
                maxVal = max(tempMax,maxVal)
                minVal = min(tempMin,minVal)
            maxCache[i][j] = maxVal
            minCache[i][j] = minVal
    print(minCache)
    print("------------")
    print(maxCache)
    return maxCache[len(matrix)-1][len(matrix[0])-1]
def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()

def main():
    matrix1 =[[-1,2,3],
              [4,5,6,],
              [7,8,9]]
    print(maxProduct(matrix1))
if __name__ =="__main__":
    main()
