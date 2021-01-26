# 11.5 COMPUTE THE REAL SQUARE ROOT

# Square root computations can be implemented using sophisticated numerical
# techniques involving iterative methods and logarithms. However, if you were
# sked to implement a square root function, you would not be expected to know
# these techniques. Implement a function which takes as input a floating
# point value and returns its square root.
#
# Hint: Iteratively compute a sequence of intervals, each contained in the
# previous interval, that contain the result.

import math

class Solution:
    def square_root(self, x: float) -> float:
        # decide search range accoridng to x's value
        left, right = (x,1.0) if x < 1.0 else (1.0,x)
        while not math.isclose(left,right):
            print("left: ",left," right: ",right)
            mid = 0.5 * (left + right)
            mid_squared = mid * mid

            if mid_squared > x:
                right = mid
            else:
                left = mid

        return left

if __name__ == "__main__":
    mySolution = Solution()
    print(mySolution.square_root(49))
