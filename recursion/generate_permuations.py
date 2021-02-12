# 15.4 GENERATE PERMUTATIONS


# This problem is concerned with computing all permutations of an array. For
# example, if the array is (2,3,5,7) one output could be (2,3,5,7), (2,3,7,5),
# (2,5,3,7), (2,5,7,3), (2,7,3,5), (2,7,5,3), (3,2,5,7), (3,2,7,5), (3,5,2,7),
# (3,5,7,2), (3,7,2,5), (3,7,5,2), (5,2,3,7), (5,2,7,3), (5,3,2,7), (5,3,7,2),
# (5,7,2,3), (5,7,2,3), (7,2,3,5), (7,2,5,3), (7,3,2,5), (7,3,5,2), (7,5,2,3),
# (7,5,3,2). (Any other ordering is acceptable too.)
# Write a program which takes as input an array of distinct integers and
# generates all permutations of that array. No permutation of the array may
# appear more than once.
#
# Hint: How many possible values are there for the first element?
from typing import List
class Solution:
    # Time complexity algorithm performs better than O(NXN!) and O(N!)
    # Space complexity : \mathcal{O}(N!)O(N!) since one has to keep N! solutions.
    def permutations(self, A:List[int]) -> List[List[int]]:
        def directed_permutaitons(i):
            if i ==len(A) -1 :
                result.append(A.copy())
                return

            # Try every possibility for A[i]
            for j in range(i,len(A)):
                A[i],A[j] = A[j],A[i]
                # Generate all permuations for A[i+1:]
                directed_permutaitons(i + 1)
                A[i], A[j] = A[j], A[i]
        result: List[List[int]] = []
        directed_permutaitons(0)
        return result


if __name__ =="__main__":
    mySolution = Solution()
    # print(len(mySolution.permutations([3])))
    # print(len(mySolution.permutations([3,4])))
    # print(len(mySolution.permutations([3,4,5])))
    print((mySolution.permutations([3,4,5,6])))
    # print(len(mySolution.permutations([3,4,5,6,7])))
    # print(len(mySolution.permutations([3,4,5,6,7,8])))
