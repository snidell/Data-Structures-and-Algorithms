# Leetcode 1499 Max Value of Equation

# Given an array points containing the coordinates of points on a 2D plane,
# sorted by the x-values, where points[i] = [xi, yi] such that xi < xj for all
# 1 <= i < j <= points.length. You are also given an integer k.
#
# Find the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k
# and 1 <= i < j <= points.length. It is guaranteed that there exists at least
# one pair of points that satisfy the constraint |xi - xj| <= k.

# Example 1:
#
# Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
# Output: 4
# Explanation: The first two points satisfy the condition |xi - xj| <= 1 and if
# we calculate the equation we get 3 + 0 + |1 - 2| = 4. Third and fourth points
# also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
# No other pairs satisfy the condition, so we return the max of 4 and 1.

from typing import List
import collections

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q = collections.deque()
        res = -float('inf')
        for x, y in points:
            print(q)
            print(x,y)
            while q and q[0][1] < x - k:
                print("q2:",q)
                q.popleft()
            if q: res = max(res, q[0][0] + y + x)
            while q and q[-1][0] <= y - x:
                q.pop()
            q.append([y - x, x])
        return res


if __name__ =="__main__":
    mySolution = Solution()

    points2 = [[-19,-12],[-13,-18],[-12,18],[-11,-8],[-8,2],[-7,12],[-5,16],[-3,9],[1,-7],[5,-4],[6,-20],[10,4],[16,4],[19,-9],[20,19]]
    k2 = 6
    print(mySolution.findMaxValueOfEquation(points2,k2))
