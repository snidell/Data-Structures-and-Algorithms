# 16 intro
# find the maximum sum over all subarrays of a given array of integers.
from typing import List

class Solution:
    # standard recursive fib sequence uses O(2^n)
    # A function to compute F(n) that recursively invokes itself has a time
    # complexity that is exponential in n
    # Space O(n) recursive call stack
    def fibinocci(self,n)-> int:
        if n <= 1:
            return n
        return self.fibinocci(n-1) + self.fibinocci(n-2)

    def fibinocciDP(self,n: int) -> int:
        if n <= 1:
            return n
        f_minus_2, f_minus_l = 0 , 1
        for _ in range(1, n):
            f = f_minus_2 + f_minus_l
            f_minus_2, f_minus_l = f_minus_l, f
        return f_minus_l
    # time spent per index is constant so O(n) time
    # recycle space here so O(1) space
    def find_max_subarray(self, A:List[int]) -> int:
        max_seen = max_end = 0
        for a in A:
            print("a:",a," a+max_end ",(a + max_end))
            max_end = max(a,a + max_end) # is this single value greater than a previous range?
            max_seen = max(max_seen,max_end) # is this value or range bigger than what we have seen before?
            print("a:",a," a+max_end ",(a + max_end),"max_end",max_end," max_seen: ",max_seen)
        return max_seen

if __name__ =="__main__":
    mySolution = Solution()
    print(mySolution.fibinocci(10))
    print(mySolution.fibinocciDP(10))
    myArray = [-2,-3,4,-10,2,-1,3]
    print(mySolution.find_max_subarray(myArray))

    print(max(-6,0))
