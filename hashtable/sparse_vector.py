
from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        self.non_zeros = {}
        for idx,num in enumerate(nums):
            if num != 0:
                self.non_zeros[idx] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for idx,num in self.non_zeros.items():
            if idx in vec.non_zeros:
                result += num * vec.non_zeros[idx]

        return result


if __name__ =="__main__":
    mySolution = SparseVector([1,0,0,2,3])
    myVector = SparseVector([0,3,0,4,0])
    print(mySolution.dotProduct(myVector))

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
