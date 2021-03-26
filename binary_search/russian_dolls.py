# Leetcode 354. Russian Doll Envelopes
# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] 
# represents the width and the height of an envelope.
#
# One envelope can fit into another if and only if both the width and height of
# one envelope is greater than the width and height of the other envelope.
#
# Return the maximum number of envelopes can you Russian doll (i.e., put one
#                                                              inside the other).
#
# Note: You cannot rotate an envelope.
#
# Example 1:
#
# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
# Example 2:
#
# Input: envelopes = [[1,1],[1,1],[1,1]]
# Output: 1
from typing import List
from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, arr: List[List[int]]) -> int:
        # sort increasing in first dimension and decreasing on second
        arr.sort(key=lambda x: (x[0], -x[1]))

        def lis(nums):
            print(nums)
            dp = []
            for i in range(len(nums)):
                idx = bisect_left(dp, nums[i])
                print(idx)
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
            print(dp)
            return len(dp)
        # extract the second dimension and run the LIS
        sec_dim = []
        for i in range(len(arr)):
            sec_dim.append(arr[i][1])
        return lis(sec_dim)


if __name__ =="__main__":
    mySolution = Solution()
    # nums = [[4,5],[4,6],[6,7],[2,3],[1,1],[1,1]]
    # nums = [[5,4],[6,4],[6,7],[2,3]]
    # this is why you cannot choose greedy approach
    # greedy picks 0,1,2,4, total of 4
    # 5 can be acheived by picking 0,1,3,6,8  ==5 total DP required
    # [[2, 100], [3, 200], [4, 300], [5, 250], [5, 400], [5, 500], [6, 360], [6, 370], [7, 380]]
    nums =[[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
    print(mySolution.maxEnvelopes(nums))
