# 1509. Minimum Difference Between Largest and Smallest Value in Three Moves
# Given an array nums, you are allowed to choose one element of nums and change
# it by any value in one move.
#
# Return the minimum difference between the largest and smallest value of nums
# after perfoming at most 3 moves.

from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        result = float("inf")
        print(nums)
        # 4 choices we can choose to:
        # 1.) convert the 3 largest
        # 2.) convert the 2 largest and 1 smallest
        # 3.) convert 1 largest and 2 smallest
        # 4.) convert the 3 smallest

        # We can realize this by by using two pointers and comparng them
        # we start with case 1 and slide that window to case 2,3,4 while
        # keeping track of what will give us a minimum
        for small,large in zip(nums[:4],nums[-4:]):
            print(large,small)
            result = min(result,large-small)

        return result


if __name__ =="__main__":
    mySolution = Solution()
    nums = [6,6,0,1,1,4,6]
    print(mySolution.minDifference(nums))
