# 16.6 THE KNAPSACK PROBLEM
# Write a program for the knapsack problem that selects a subset of items that
# has maxinmm value and satisfies the weight constraint. All items have integer
# weights and values. Return the value of the subset.
#
# Hint: Greedy approaches are doomed.

import collections
from typing import List
Item = collections.namedtuple('Item',('weight','value'))
class Solution:
    # Bottom up solution space and time are O(n*m) where n is the capacity and m is the length of items
    def knapsack(self,items:List[Item],capacity:int)->int:
        n = len(items)
        K = [[0 for x in range(capacity + 1) ] for x in range(n + 1)]
        for i in range(n +1):
            for w in range(capacity + 1):
                if i == 0 or w ==0:
                    K[i][w] = 0
                elif items[i-1].weight <= w:
                    K[i][w] = max(K[i-1][w],items[i-1].value + K[i-1][w - items[i-1].weight])
                else:
                    K[i][w] = K[i][w]
        return K[n][capacity]


if __name__ =="__main__":
    mySolution = Solution()
    myItem1 = Item(1,1)
    myItem2 = Item(3,4)
    myItem3 = Item(4,5)
    myItem4 = Item(5,7)
    capacity = 7
    print("the max value we can generate from a capacity of ",capacity, " is:")
    print(mySolution.knapsack([myItem1,myItem2,myItem3,myItem4],capacity))

# target -> 1, 2, 3, 4, 5, 6, 7, 8
        # 0[0, 0, 0, 0, 0, 0, 0, 0]
        # 1[0, 1, 1, 1, 1, 1, 1, 1]
        # 3[0, 0, 0, 4, 5, 5, 5, 5]
        # 4[0, 0, 0, 0, 5, 5, 5, 9]
        # 5[0, 0, 0, 0, 0, 7, 7, 9]
