# 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum
# Given an array of integers arr and an integer target.
#
# You have to find two non-overlapping sub-arrays of arr each with a sum equal
# target. There can be multiple answers so you have to find an answer where the
# sum of the lengths of the two sub-arrays is minimum.
#
# Return the minimum sum of the lengths of the two required sub-arrays, or
# return -1 if you cannot find such two sub-arrays.

# Input: arr = [3,2,2,4,3], target = 3
# Output: 2
# Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their
# lengths is 2.


from typing import List
import math
import itertools

class Solution:
    # run time is 2*O(N) O(N) for acumulate and O(n) for providing the answer
    # space: O(N) for the DP cache
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # maps current value to index
        prefix = {0: -1}
        # dp array that holds the best index to get to sum target
        best_till = [math.inf] * len(arr)
        # result holds the minimum sum of the lengths
        # best holds the best answer for the particular iteration
        result = best = math.inf
        # itertools.accumulate runs in O(n) and sums up to the array to provide previx sum
        for i, curr in enumerate(itertools.accumulate(arr)):
            if curr - target in prefix:
                end = prefix[curr - target]
                if end > -1:
                    result = min(result, i - end + best_till[end])
                best = min(best, i - end)
            best_till[i] = best
            prefix[curr] = i
        print(best_till)
        return -1 if result == math.inf else result


if __name__ =="__main__":
    mySolution = Solution()
    myArray = [6,6,6,4,3]
    target = 3
    print(mySolution.minSumOfLengths(myArray,target))
