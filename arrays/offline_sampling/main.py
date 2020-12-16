# 5.12 SAMPLE OFFLINE DATA
import random
class Solution():
    def random_sampling(self,k:int, A: [int]) -> None:
        for i in range(k):
            r = random.randint(i,len(A)-1)
            A[i], A[r] = A[r], A[i]
        print(A[:k])




if __name__ == "__main__":
    mySolution = Solution()
    mySolution.random_sampling(3,[1,2,3,4,5,6,7,8,9,10])
