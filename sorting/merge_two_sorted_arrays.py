# 13.2 Merge two sorted arrays

# Write a program which takes as input two sorted arrays of integers, and
# updates the first to the combined entries of the two arrays in sorted order.
# Assume the first array has enough empty entries at its end to hold the result.
#
# Hint: Avoid repeatedly moving entries.
# in this case len(A) >= len(B)+ A(populated values)
# Leetcode 88 (easy)
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one
# sorted array.
#
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has a size equal to m + n such that it has enough
# space to hold additional elements from nums2.
from typing import List
class Solution:
    def merge(self,A:List[int],m:int, B:List[int],n:int)-> List[int]:
        # insert from the end of A
        p1 = m - 1
        p2 = n -1

        # iterate m+m-1 times starting at the last index (-1) and proceeding
        # backward through the array (-1)
        for p in range(m+n-1, -1, -1):
            print("p: ",p," A[p1]: ",A[p1]," B[p2]",B[p2])
            # if we have exhausted all in B break
            if p2 < 0:
                break
            # if we haven't exhuasted all numbers in A and A is bigger
            # than grab that one
            if p1 >= 0 and A[p1] > B[p2]:
                A[p] = A[p1]
                p1 -= 1
            else:
                A[p] = B[p2]
                p2 -= 1
        return A




if __name__ == "__main__":
    # Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    # Output: [1,2,2,3,5,6]
    mySolution = Solution()
    A = [2,5,6,0,0,0]
    B = [1,2,3]
    print(mySolution.merge(A,3,B,3))
