# https://leetcode.com/problems/two-sum/
# Given an array of integers nums and and integer target, return the indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
def twoSum(self, nums: List[int], target: int) -> List[int]:
    map ={}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in map.keys():
            return [map[complement],i]
        map[nums[i]] = i


if __name__ == "__main__":
    myNums = [1,2,3,4,5,6,7]
    print(twoSum(nums=myNums, target=8))
