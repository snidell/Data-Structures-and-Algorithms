# 11.7 FIND THE MIN AND MAX SIMULTANEOUSLY
# Given an array of comparable objects, you can find either the min or the max of
# the elements in the array with n - 1 comparisons, where n is the length of the
# array.
# Comparing elements may be expensive, e.g., a comparison may involve a number
# of nested calls or the elements being compared may be long strings. Therefore,
# it is natural to ask if both the min and the max can be computed with less
# than the 2(n - 1) comparisons required to compute the min and the max
# independently.

# Design ai1 algorithm to find the min and max elements in an array. For
# example, if A = (3, 2, 5, 1, 2, 4), you should return 1 for the min and
# 5 for the max.

 # Hint: Use the fact that a < b and b < c implies a < c to reduce the number of
 # compares used by the brute-force approach.
import collections
from typing import List

MinMax = collections.namedtuple('MinMax',('smallest','largest'))
class Solution:
    #  The time complexity is O(n) and the space complexity is 0(1)
    def find_max(self, A: List[int]) -> MinMax:
        def min_max(a,b)-> MinMax:
            return MinMax(a,b) if a< b else MinMax(b,a)

        if len(A) <= 1:
            return MinMax(A[0],A[0])
        global_min_max = min_max(A[0],A[1])

        for i in range(2,len(A) -1,2):
            local_min_max = min_max(A[i],A[i+1])
            global_min_max = MinMax(
                min(global_min_max.smallest,local_min_max.smallest),
                max(global_min_max.largest,local_min_max.largest))

        # If there is an odd number of elements in the array we still need to
        # compare the last element with the existing answer

        if len(A) % 2:
            global_min_max = MinMax(min(global_min_max.smallest,A[-1]),
                                    max(global_min_max.largest,A[-1]))
        return global_min_max


if __name__ == "__main__":
    mySolution = Solution()
    print(mySolution.find_max([1,2,3,4,10,-3,4,5,6,44]))
    # MinMax(smallest=-3, largest=44)
