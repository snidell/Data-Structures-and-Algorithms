#  11.1 SEARCH A SORTED ARRAY FOR FIRST OCCURRENCE OF k

# Write a method that takes a sorted array and a key and returns the index of
# the first occurrence of that key in the array. Return -1 if the key does not
# appear in the array. For example, when applied to the array in Figure 11.1
# your algorithm should return 3 if the given key is 108; if it is 285, your
# algorithm should return 6.

# Hint: What happens when every entry equals k? Don't stop when you first seek.
from typing import List
class Solution:
    def search_first_k(self, A: List[int],k:int) -> int:
        left, right, result = 0, len(A) - 1, -1
        while   left <= right:
            mid = (left+right) // 2

            if A[mid] >k:
                right = mid -1
            elif A[mid] == k:
                result = mid
                right = mid  -1 # nothing to the right keep the solution
            else:
                # A[mid] < k
                left = mid +1
        return result

if __name__ == "__main__":

    mySolution = Solution()
    print("the index of the first occurence is: ",mySolution.search_first_k([-14,-10,2,108,108,243,285,285,285,401],108))
    print("the index of the first occurence is: ",mySolution.search_first_k([-14,-10,2,108,108,243,285,285,285,401],285))
    print("the index of the first occurence is: ",mySolution.search_first_k([-14,-10,2,108,108,243,285,285,285,401],7))
