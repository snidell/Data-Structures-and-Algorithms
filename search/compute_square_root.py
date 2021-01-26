# 11.4 COMPUTE THE INTEGER SQUARE ROOT

# Write a program which takes a nonnegative integer and reh1rns the largest
# integer whose square is less than or equal to the given integer. For example,
# if the input is 16, return 4; if the input is 300,
# return 17, since 172 = 289 < 300 and 182 = 324 > 300.

# Hint: Look out for a corner-case.

class Solution:
    def compute_sq_root(self, k:int) -> int:
        left, right = 0, k
        # Candidate interval [left,right] where everything before the left has square
        # <= k everything after right has square > k

        while left <= right:
            mid = (left + right) // 2
            mid_squared = mid * mid
            if mid_squared <= k:
                left = mid + 1
            else:
                right = mid -1
        return left -1

if __name__ =="__main__":
    mySolution = Solution()
    print(mySolution.compute_sq_root(33))
