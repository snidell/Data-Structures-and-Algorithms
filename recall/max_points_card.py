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
#
#
# Input: cardPoints = [1,2,3,4,5,6,1], k = 3
# Output: 12
# Explanation: After the first step, your score will always be 1. However,
# choosing the rightmost card first will maximize your total score. The optimal
# strategy is to take the three cards on the right, giving a final score of
# 1 + 6 + 5 = 12.

from typing import List

class Solution():
    def maxScore(self,cardPoints: List[int],k:int) -> int:
        # start from the last 3 items and sum them together
        current = sum(cardPoints[k+1:])
        current_max = current
        for i in range(1,k+1):
            # increment the two pointers and slide right from both ends
            # subtract right number and add left number
            current = current - sum(cardPoints[:(k+1+i)]) + sum(cardPoints[:i])
            current_max = max(current_max,current)
        # keep a global max number and compare
        return current_max



if __name__ =="__main__":
    mySolution = Solution()
    cards = [1,2,3,4,5,6,1]
    k = 3
    print(mySolution.maxScore(cards,k))
