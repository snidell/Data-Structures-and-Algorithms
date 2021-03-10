
# There are several cards arranged in a row, and each card has an associated
# number of points The points are given in the integer array cardPoints.
#
# In one step, you can take one card from the beginning or from the end of the
# row. You have to take exactly k cards.
#
# Your score is the sum of the points of the cards you have taken.
#
# Given the integer array cardPoints and the integer k, return the maximum score
# you can obtain.

# Input: cardPoints = [1,2,3,4,5,6,1], k = 3
# Output: 12
# Explanation: After the first step, your score will always be 1. However,
# choosing the rightmost card first will maximize your total score. The optimal
# strategy is to take the three cards on the right, giving a final score
# of 1 + 6 + 5 = 12.

from typing import List

class Solution:
    # time complexity is O(k) as we iterated through k choices
    # space complexity is O(1)
    def maxScore(self,cardPoints: List[int],k: int)-> int:
        size = len(cardPoints)
        left, right = k-1 , size-1
        currentSum = sum(cardPoints[:k])
        currentMax = currentSum

        for _ in range(k):
            print(currentSum,"+= ",cardPoints[right]," + ",cardPoints[left])
            currentSum += (cardPoints[right] - cardPoints[left])
            currentMax = max(currentMax,currentSum)

            left, right = left - 1, right - 1

        return currentMax



if __name__ =="__main__":
    mySolution = Solution()
    print(mySolution.maxScore([1,2,3,4,5,6,1],3))
    myDict = {0:[1,2,3,4,5,6,1]}
    print(myDict[0])

    myList = [[1,2],[3,4],[6,10]]

    for i in myList:
        print(i)


# class MyCalendar:
#
#     def __init__(self):
#         self.events = []
#
#
#     def book(self, start: int, end: int) -> bool:
#         for event in self.events:
#             if (event[0]< start and event[1] >start) or \
#             (event[0]<end and event[1]>end) or \
#             (start <= event[0] and end >= event[1]):
#                 return False
#         self.events.append([start,end])
#         return True
