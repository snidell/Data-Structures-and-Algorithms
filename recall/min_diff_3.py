
from typing import List
class Solution:
    def get_min_three(self,nums:List[int])->int:
        # sort
        nums.sort()
        # catch case where
        # use two pointers and compare the result starting with 3+1 point so
        result = float("inf")
        ptr1 = 0
        print(range(len(nums)-4,len(nums)))
        for ptr2 in range(len(nums)-4,len(nums)):
            current_min = nums[ptr2] - nums[ptr1]
            result = min(result,current_min)
            ptr1+=1

        return result
        # we sort like this [0,1,5,10,14] pointer would be 0,1, then 1,5, then 5-10
        # keep min in result, update with every new change

        return 0




if __name__ =="__main__":
    mySolution = Solution()
    nums = [6,6,0,1,1,4,6]
    print(mySolution.get_min_three(nums))
