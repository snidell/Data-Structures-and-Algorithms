# 16.12 FIND THE LONGEST NONDECREASING SUBSEQUENCE
# Write a program that takes as input an array of numbers and returns the
# length of a longest nondecreasing subsequence in the array.
# Hint: Express the longest nondecreasing subsequence ending at an entry in
# terms of the longest nondecreasing subsequence appearing in the subarray
# consisting of preceding elements.
# Explanation: https://www.youtube.com/watch?v=fV-TF4OvZpk

from typing import List

class Solution:
    def longest_nondecreasing_subsequence(self,A: List[int])->List[int]:
        # max_length holds the length of the longest nondecreasing subsequence
        # of A[:i + 1]
        dp = [1] * len(A)

        for i in range(1,len(A)):
            max = 0
            for j in range(i):
                if A[i] >= A[j]:
                    max = dp[j]
            # max_length[i] = 1 + max((dp[j] for j in range(i) if A[i] >=A[j]),default = 0)
            dp[i] = 1 + max
        return dp

if __name__ =="__main__":
    mySolution = Solution()
    dp = mySolution.longest_nondecreasing_subsequence([1,2,3,2,3,4,5,6,7,8])
    print(dp)
    print(max(dp))
