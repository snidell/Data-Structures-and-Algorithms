
# 13.1 COMPUTE THE INTERSECTION OF TWO SORTED ARRAYS

# Write a program which takes as input two sorted arrays, and returns a new array
# containing elements that are present in both of the input arrays. The input
# arrays may have duplicate entries, but the returned array should be free of
# duplicates. For example, the input is (2, 3, 3, 5, 5, 6, 7, 7,8, 12) and
# (5, 5, 6, 8, 8, 9, 10, 10), your output should be (5, 6, 8).

from typing import List
import bisect

class Solution:
    # this is most efficent if B is siginificantly greater than A
    def intersection(self,A:List[int], B: List[int])-> List[int]:
        # perform
        def is_present(k):
            i = bisect.bisect_left(B,k)
            return i < len(B) and B[i] == k

        result = []

        for i, a in enumerate(A):
            if is_present(a):
                result.append(a)
        return result
    def equal_intersection(self,A:List[int],B:List[int])-> List[int]:
        result = []
        i = j =0
        while i <len(A) and j < len(B):
            if A[i] == B[j]:
                result.append(A[i])
                i, j, = i+1 , j+1
            elif A[i] < B[j]:
                i += 1
            else:
                j += 1
        return result


if __name__ =="__main__":
    mySolution = Solution()
    A = [1,2,3,4,5,6,7,8,90,92]
    B = [1,1,1,4,6,7,8,9,12,33,38,90]
    print(mySolution.intersection(A,B))

    print(mySolution.equal_intersection(A,B))
