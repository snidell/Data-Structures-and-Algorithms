
import collections
from typing import List

class Solution:
    def __init__(self, A: List[int]):
        self.pointer = 0
        self.nums = []
        self.repetitions = []
        for i in range(0, len(A) - 1, 2):
            repetition, num = A[i], A[i + 1]
            # avoid empty nums
            if repetition:
                self.nums.append(num)
                self.repetitions.append(repetition)

    def next(self, n: int) -> int:
        # chekc if we supass
        while n:
            # check index out of range
            if self.pointer == len(self.repetitions):
                return -1
            # move pointer
            if n > self.repetitions[self.pointer]:
                # reduce n
                n -= self.repetitions[self.pointer]
                # move pointer to next num
                self.pointer += 1
            else:
                # reduce repetitions left
                self.repetitions[self.pointer] -= n
                n = 0
        return self.nums[self.pointer]

if __name__ =="__main__":
    mySolution = Solution([3,8,0,9,2,5])
    print(mySolution.next(2)) # 8
    print(mySolution.next(1)) # 8
    print(mySolution.next(1)) # 5
    print(mySolution.next(2)) # -1


    
