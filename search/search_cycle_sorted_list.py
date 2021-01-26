#
# 11.3 SEARCH A CYCLICALLY SORTED ARRAY
#
# An array is said to be cyclically sorted if it is possible to cyclically shift
# its entries so that it becomes sorted. For example, the array in Figure 11.2
# is cyclically sorted-a cyclic left shift by 4 leads to a sorted array.

# normal sorted list     [103,203,220,234,279,368,378,478,550,661]
# cyclically sorted list [378,478,550,661,103,203,220,234,279,368]

# Design an O(log n) algorithm for finding the position of the smallest element
# in a cyclically sorted array. Assume all elements are distinct. For example,
# for the array in Figure 11.2, your algorithm should return 4.
# Hint: Use the divide and conquer principle.

# Leetcode
# 153. Find Minimum in Rotated Sorted Array
# Suppose an array of length n sorted in ascending order is rotated between 1
# and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
#
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.

from typing import List

class Solution:
    def find_smallest(self, A: List[int]) -> int:
        left, right = 0, len(A) - 1
        while left < right:
            mid = (left+right) // 2
            print("left: ",left," mid: ",mid," right: ",right)
            if A[mid] > A[right]:
                # miniumn must be in A[mid + 1: right + 1]
                left = mid +1
            else:
                #  minimum cannot be in A[mid + 1: right + 1] so it must be
                # in A[left: mid +1]
                right = mid
        return left

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def find_rotate_index(left, right):
            if nums[left] < nums[right]:
                return 0

            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot - 1
                    else:
                        left = pivot + 1

        def search(left, right):
            """
            Binary search
            """
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] == target:
                    return pivot
                else:
                    if target < nums[pivot]:
                        right = pivot - 1
                    else:
                        left = pivot + 1
            return -1

        n = len(nums)

        if n == 1:
            return 0 if nums[0] == target else -1

        rotate_index = find_rotate_index(0, n - 1)

        # if target is the smallest element
        if nums[rotate_index] == target:
            return rotate_index
        # if array is not rotated, search in the entire array
        if rotate_index == 0:
            return search(0, n - 1)
        if target < nums[0]:
            # search on the right side
            return search(rotate_index, n - 1)
        # search on the left side
        return search(0, rotate_index)

if __name__ == "__main__":
    mySolution = Solution()
    # returns 4
    print(mySolution.find_smallest([378,478,550,661,103,203,220,234,279,368]))
    print(mySolution.find_smallest([378,478,550,661,103,203,220,234,279,368]))
    print("search for 103 the index is: ",mySolution.search([378,478,550,661,103,203,220,234,279,368],103))
