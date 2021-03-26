# Leetcode 315. Count of Smaller Numbers After Self
# You are given an integer array nums and you have to return a new counts array.
# The counts array has the property where counts[i] is the number of smaller
# elements to the right of nums[i].
#
# Example 1:
#
# Input: nums = [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
#
# Example 2:
#
# Input: nums = [-1]
# Output: [0]
# Example 3:
#
# Input: nums = [-1,-1]
# Output: [0,0]
from typing import List
import bisect
class Solution:
    def count_smaller(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        s_nums = sorted(nums)

        print("s_nums: ",s_nums)
        for idx,n in enumerate(nums):
            j = bisect.bisect_left(s_nums, n) # returns idx of the leftmost occurrence of n...
            print("n:",n," j:",j)
            res[idx] = j               # ...so all elements to its left are smaller
            s_nums.pop(j)              # remove it so next numbers to the right don't take it into account

        return res




if __name__ =="__main__":
    mySolution = Solution()
    nums = [5,2,6,1]
    print("nums: ",nums)
    print(mySolution.count_smaller(nums))
