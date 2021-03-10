
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not
#  use the same element twice.
#
# You can return the answer in any order.

from typing import List
class Solution:
    def twoSum(self,nums:List[int],target:int)-> List[int]:
        # key = compliment value = index
        compliment = {}
        for i in range(len(nums)):
            # we have a match
            tempCompliment = (target - nums[i])
            if  tempCompliment in compliment:
                return [compliment[target - nums[i]],i]
            else:
                compliment[nums[i]] = i
        return []


if __name__ =="__main__":
    mySolution = Solution()
    print(mySolution.twoSum([2,7,11,15],9))
