from typing import List

class Solution:
    def bsearch(self, t: int, A: List[int]) ->int:
        L, U, = 0, len(A) - 1
        while L <= U:
            M =  L + (U - L) // 2
            if A[M] < t:
                L = M + 1
            elif A[M] == t:
                return M
            else:
                U = M - 1
        return -1


if __name__ =="__main__":
    mySolution = Solution()
    # returns the index of where 4 resides
    print(mySolution.bsearch(4,[1,2,3,4,5,6,7,8,9,10,11]))
