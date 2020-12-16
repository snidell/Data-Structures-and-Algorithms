
from typing import List
class Solution:
    def insertion_sort(self,A: List[int])->List[int]:
        for i in range(1,len(A)):
            current_value = A[i] # value 4 right now
            j=i-1 # index 0 value 5

            # while there is some array left and the current value is smaller
            # keep swapping
            while j>=0 and A[j]>current_value:
                A[j+1] = A[j]
                j=j-1
            A[j+1] = current_value
        return A
if __name__ == "__main__":
    mySolution = Solution()
    print(mySolution.insertion_sort([5,4,3,2,1]))
