# 17.4 3-SUM
# Design an algorithm that takes as input an array and a number, and determines
# if there are three entries in the array (not necessarily distinct) which add up
# to the specified number. For example, if the array is (11, 2,5, 7,3) then there
# are three entries in the array which add up to 21 (3, 7, 11 and 5, 5, 11).
# (Note that we can use 5 twice, since the problem statement said we can use the
# same entry more than once.) However, no three entries add up to 22.
#
# Hint: How would you check if a given array entry can be added to two more
# entries to get the specified number?

from typing import List

class Solution:
    def has_two_sum(self,A: List[int], t: int) -> bool:
        i, j =0, len(A) - 1
        while i <= j:
            if A[i] + A[j] == t:
                return True
            elif A[i] + A[j] < t:
                i += 1
            else: # A[i] + A[j] > t.
                j -= 1
        return False

    def three_sum(self,A:List[int],t:int)->bool:
        A.sort()
        return any(self.has_two_sum(A,t-a) for a in A)
    # Given an array nums of n integers, are there elements a, b, c in nums such
    # that a + b + c = 0? Find all unique triplets in the array which gives the
    # sum of zero.
    #
    # Notice that the solution set must not contain duplicate triplets.
    # example
    # Input: nums = [-1,0,1,2,-1,-4]
    # Output: [[-1,-1,2],[-1,0,1]]
    # Leetcode 15: threeSum
    # Time complexity O(n^2) twoSum is O(n) and we call it n times
    # Space complexity  O(n) for dictionary of twoSum
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)
        return res
    # single pass of numbers with hashmap for compliment
    # Time Complexity O(n)
    # Space complexity O(n) numbers stored in hastable
    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
        seen = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1

if __name__ =="__main__":
    mySolution = Solution()
    print(mySolution.three_sum([1,2,3,4,5,6,8,12],10))
    # lists of numbers that add up to zero
    print(mySolution.threeSum([-1,0,1,2,-1,-4]))
