# https://www.byte-by-byte.com/01knapsack/?utm_source=optin_carrot&utm_medium=pdf&utm_campaign=50questions
from collections import defaultdict


def naiveKnapsack(weights, values, maxWeight, i=0):
    if len(weights) == i:
        return 0
    # if the item is too big for the target weight with the current
    # weight move to next combination
    if maxWeight - weights[i] < 0:
        return naiveKnapsack(weights, values, maxWeight, i + 1)
    # Try to take item and exlcude item to see which gives best result
    return max(naiveKnapsack(weights, values, maxWeight - weights[i], i + 1) + values[i],
                naiveKnapsack(weights, values, maxWeight, i + 1))


def topDown(weights, values, maxWeight, i=0, cache=defaultdict()):
    if len(weights) == i:
        return 0
    # if the item is not cached put it in cache
    if i not in cache:
        newDict = defaultdict()
        cache.update({i: newDict})
    cached = cache.get(i).get(maxWeight)
    # use cache if we have seen that value before
    if cached is not None:
        return cached
    # if item is heavier than remainder skip it
    if maxWeight - weights[i] < 0:
        return topDown(weights, values, maxWeight, i + 1, cache)
    # try both including and excluding current weight values
    currentMax = max(topDown(weights, values, maxWeight - weights[i], i + 1, cache) + values[i],
                topDown(weights, values, maxWeight, i + 1, cache))

    cache.get(i).update({maxWeight: currentMax})
    return currentMax


def createCache(rows, columns, value):
    matrix = [[value for i in range(columns)]
                for i in range(rows)]
    return matrix


def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()


def bottomUp2(W, wt, val, n):
    K=[[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n+1):
        for w in range(W+1):
            if i ==0 or w ==0:
                K[i][w]=0
            elif wt[i-1]<=w:
                #if the current weight under inspeciton is smaller than the current weight
                #take the max of the current weight/val and its remainder or take directly
                #from above row
                K[i][w] = max(K[i-1][w],val[i-1]+K[i-1][w-wt[i-1]])
            else:
                #Current weight is too big for target weight so take the best above row
                K[i][w] = K[i-1][w]
    #We are finished with the matrix the optiumal solution always exists in the bottom right corner
    printMatrix(K)
    return K[n][W]

def bottomUp(W, wt, val, n):
   K = [[0 for x in range(W + 1)] for x in range(n + 1)]
   # Table in bottom up manner
   for i in range(n + 1):
      for w in range(W + 1):
         if i == 0 or w == 0:
            K[i][w] = 0
         elif wt[i - 1] <= w:
            print("I: ", i, " w: ", w)
            # print("K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])")
            print("val[i-1] + K[i-1][w-wt[i-1]]")
            print(val[i - 1], " ", K[i - 1][w - wt[i - 1]])
            print("K[i-1][w-wt[i-1]]")
            print(w, wt[i - 1], w - wt[i - 1])
            # print(max(val[i-1] + K[i-1][w-wt[i-1]],K[i-1][w])," ",val[i-1] + K[i-1][w-wt[i-1]]," ",K[i-1][w])
            K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
         else:
            K[i][w] = K[i - 1][w]

   printMatrix(K)
   return K[n][W]



def main():
    # Given a list of items with values and weights, as well as a max weight,
    # find the maximum value you can generate from items where the sum of the
    # weights is less than the max.
    weights= [1, 3, 4, 5]
    values= [1, 4, 5, 7]
    maxWeight = 7
    n = len(values)
    # print(naiveKnapsack(weights,values, maxWeight))
    # print(topDown(weights,values,maxWeight))
    print(bottomUp2(maxWeight,weights,values,n))
    #print(bottomUp(maxWeight,weights,values,n))



if __name__ == "__main__":
    main()
