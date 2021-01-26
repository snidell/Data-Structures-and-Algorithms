# 11.10 FIND The DUPLICATE AND MISSING ELEMENTS
# Instead of using the book description and solution we are using leetcodes
# solution to finding a duplicate and finding a missing element.
# this way we can solve them indepently if needed or combined them if they show
# up as the text form

# Leetcode 268 Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return
# the only number in the range that is missing from the array.
#
# Follow up: Could you implement a solution using only O(1) extra space
# complexity and O(n) runtime complexity?

from typing import List

class Solution:
    # sorting + two pointers Nlog(N) time complexity O(1) space
    def missingNumberSort(self, nums: List[int]) -> int:
        nums.sort()

        # ensure that n is at the last node
        if nums[-1] != len(nums):
            return len(nums)
        # ensure that 0 is at the first index
        elif nums[0] !=0:
            return 0

        # if we get here the missing number is on the range of (0,n)
        for i in range (1,len(nums)):
            expected_num = nums[i-1] +1
            if nums[i] != expected_num:
                return expected_num
    # time O(n) space O(n)
    def missingNumberSet(self, nums:List[int]) -> int:
        num_set = set(nums)
        n = len(nums) +1
        for number in range(n):
            if number not in num_set:
                return number
    # time complexity O(n) space O(1)
    # Because we know that nums contains nn numbers and that it is missing
    # exactly one number on the range [0..n-1][0..n−1], we know that nn
    # definitely replaces the missing number in nums. Therefore, if we
    # initialize an integer to nn and XOR it with every index and value, we will
    # be left with the missing number. Consider the following example
    # (the values have been sorted for intuitive convenience, but need not be):
    # index: 0 ,1 ,2 ,3
    # value: 0 ,1 ,3 ,4
    # missing =4∧(0∧0)∧(1∧1)∧(2∧3)∧(3∧4)
    #         =(4∧4)∧(0∧0)∧(1∧1)∧(3∧3)∧2
    #         =0∧0∧0∧0∧2
    #         =2

    def missingNumberBit(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing^= i ^ num
        return missing

    # 287. Find the Duplicate Number
    # Given an array of integers nums containing n + 1 integers where each integer
    # is in the range [1, n] inclusive.
    #
    # There is only one repeated number in nums, return this repeated number.

    # Proving that at least one duplicate must exist in nums is simple application
    # of the pigeonhole principle. Here, each number in nums is a "pigeon" and each
    # distinct number that can appear in nums is a "pigeonhole". Because there are
    # n+1n+1 numbers are nn distinct possible numbers, the pigeonhole principle
    # implies that at least one of the numbers is duplicated.
    # time complexity Nlog(n) space O(1)
    def findDuplicateSort(self,nums: List[int]) -> int:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                return nums[i]

    # time complexity is O(n) space is O(n)
    def findDuplicateSet(self, nums:List[int]) -> int:
        set_nums = set()

        for num in nums:
            if num in set_nums:
                return num
            set_nums.add(num)
    # Floyd's Tortoise and Hare (Cycle Detection)
    # idea is to reduce to a link list and return node where cycle begins
    # First of all, where does the cycle come from? Let's use the function
    # f(x) = nums[x] to construct the sequence: x, nums[x], nums[nums[x]],
    # nums[nums[nums[x]]], ....
    #
    # Each new element in the sequence is an element in nums at the index of the
    # previous element.
    #
    # If one starts from x = nums[0], such a sequence will produce a linked list
    # with a cycle.
    def findDuplicateFloyd(self, nums):
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        print("tortoise: ",tortoise," hare: ",hare)
        while True:
            tortoise = nums[tortoise] # tortoise = 6,5,6
            hare = nums[nums[hare]]    # hare = 6,6,6  nums[nums[6]] =nums[5] = 6 nums[nums[6]] -> nums[5]->6
            print("tortoise: ",tortoise," hare: ",hare)
            if tortoise == hare:
                break

        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare




if __name__ =="__main__":
    mySolution = Solution()
    print("the missing number is: ",mySolution.missingNumberSort([0,1,2,3,4,6]))
    print("the missing number is: ",mySolution.missingNumberSet([0,1,2,3,4,6]))
    print("the missing number is: ",mySolution.missingNumberBit([0,1,2,3,4,6]))
    print("")
    print("the duplicate is(sort): ",mySolution.findDuplicateSort([1,2,3,4,4,5,6]))
    print("the duplicate is(set): ",mySolution.findDuplicateSet([1,2,3,4,4,5,6]))
    print("the duplicate is(floyd): ",mySolution.findDuplicateFloyd([6,1,4,3,2,6,5]))
