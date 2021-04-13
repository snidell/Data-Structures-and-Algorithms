# 15.5 GENERATE THE POWER SET

# The power set of a set S is the set of all subsets of S, including both the
# empty set 0 and S itself. The power set of {O, 1, 2} is graphically
# illustrated in Figure 15.6.

# Write a function that takes as input a set and returns its power set.
# Hint: There are 2" subsets for a given set S of size n. There are
# i' k-bit words.

from typing import List

class Solution:
    # Time complexity O(N x N^2) to generate all subsets and then copy them into output list.
    # Space O(N x N^2) This is exactly the number of solutions for subsets
    # multiplied by the number NN of elements to keep for each subset.
    def cascade(self,nums:List[int])->List[List[int]]:
        n = len(nums)
        # initialize with empty set
        output=[[]]
        for num in nums:
            output += [curr + [num] for curr in output]
        return output

    # time complexity O(N x N^2) to generate all subset and copy them into
    # output list
    # space complexity O(N x X^2) to keep all subsets of length N
    def lexigraphic_subset(self,nums:List[int])->List[List[int]]:
        n = len(nums)
        output = []
        for i in range(2**n,2**(n+1)):
            # why [3:] ? it removes the 0bsign of the binary number 0b1 which
            # isn't needed here
            print(i)
            bitmask = bin(i)[3:]
            print(bitmask)
            # append subset to that bitmask
            number = []
            for j in range(n):
                if bitmask[j] =='1':
                    number.append(nums[j])
            print(number)
            output.append(number)
        return output

if __name__ =="__main__":
    mySolution = Solution()
    # print(mySolution.cascade([1,2,3]))
    myArray = range(1,4) #good up to some huge number 10billion or so
    print(mySolution.lexigraphic_subset(myArray))
    # 000
    # 001
    # 010
    # 011
    # 100
    # 101
    # 110
    # 111
    # [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
