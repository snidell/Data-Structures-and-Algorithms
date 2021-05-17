
from typing import List

class Solution:
    def __init__(self,A:List[int]):
        self.nums = []
        self.repititions = []
        self.pointer = 0
        for i in range(len(A)-1):
            nums,repitiions = A[i+1],A[i]
            if repitiions:
                self.nums.append(nums)
                self.repititions.append(repitiions)


    def next(self,n:int)-> int:
        # decement n until it is empty
        while n:
            # base case we are out of numbers:
            if self.pointer == len(self.nums):
                return -1
            if n > self.repititions[self.pointer]:
                n - self.repititions[self.pointer]
                self.pointer += 1
            else:
                self.repititions[self.pointer] -= n
                n = 0


        return self.nums[self.pointer]



if __name__ =="__main__":
    mySolution = Solution([3,8,0,9,2,5])
    print(mySolution.next(2))
    print(mySolution.next(200))
