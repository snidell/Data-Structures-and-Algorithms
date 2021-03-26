# Leetcode 552. Student Attendance Record II
#
# An attendance record for a student can be represented as a string where each
# character signifies whether the student was absent, late, or present on that
# day. The record only contains the following three characters:
#
# 'A': Absent.
# 'L': Late.
# 'P': Present.
# Any student is eligible for an attendance award if they meet both of the
# following criteria:
#
# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Given an integer n, return the number of possible attendance records of length
# n that make a student eligible for an attendance award. The answer may be very
# large, so return it modulo 109 + 7.
#
# Example 1:
#
# Input: n = 2
# Output: 8
# Explanation: There are 8 records with length 2 that are eligible for an award:
# "PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" is not eligible because there are 2 absences (there need to be fewer
#                                                         than 2).
# Example 2:
#
# Input: n = 1
# Output: 3




class Solution:
    def checkRecord(self, n: int) -> int:
        # dptotal[i] the number of rewardable records without A whose lenghth is i
        dptotal = [0] *  (n + 1)
        dp1,dp2,dp3 = 1,1,0
        # dp1: the number of rewardable records that end with one L and without A
        # dp2: the number of rewardable records that end with one P and without A
        # dp3: the number of rewardable records that end with two Ls and without A
        dptotal[0] = 1 #
        dptotal[1] = dp1 + dp2 + dp3
        mod = 10**9 +7
        for i in range(2,n+1):
            dp1,dp2,dp3 = dp2 % mod,(dp1+dp2+dp3) % mod,dp1 % mod
            dptotal[i] = (dp1 + dp2 + dp3) % mod
        print(dptotal)
        res = 0
        res += dptotal[-1]
        # take A into consideration:
        # A can take n location
        for i in range(n):
            # i is the location of A
            res += (dptotal[n-i-1] * dptotal[i]) % mod
        return res % mod

        


if __name__ =="__main__":
    mySolution = Solution()
    n = 10
    print("number of combination given ",n," days ",mySolution.checkRecord(n))
