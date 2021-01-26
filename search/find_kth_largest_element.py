# 11.8 FIND THE kTH LARGEST ELEMENT
# For example, if the input array A = (3, 2, 1,5,4), then A[3] is the first
# largest element (k = 1) in A, A[O] is the third largest element (k = 3) in
# A, and A[2] is the fifth largest element (k = 5) in A. The input array may
# have duplicates, e.g., (3, 2, 5, 3, 5)-the first and second largest elements
# are both 5; the third and fourth largest elements are 3; and the fifth largest
# element is 2.
#
# Design an algorithm for computing the kTH largest element in an array. Assume
# entries are distinct. Hint: Use divide and conquer in conjunction with
# randomization.

# Leetcode 215  Kth Largest Element in an Array
from typing import List
import random
import heapq
class Solution:
    # using quickselect and pivot
    # Time complexity : O(N) in the average case, (N^2) in the worst case.
    # Space complexity : O(1).
    def findkthLargest(self, A:List[int], k:int) -> int:
            def partition(left,right,pivot_index):
                pivot = A[pivot_index]
                # move pivot to the end
                A[pivot_index], A[right] = A[right], A[pivot_index]

                # move all smaller elements to the left
                store_index = left
                for i in range(left,right):
                    if A[i] < pivot:
                        A[store_index] = A[i]
                        store_index += 1

                # move the pivot back to where i should be
                A[right], A[store_index] = A[store_index], A[right]
                return store_index

            def select(left,right,k_smallest):
                if left == right:
                    return A[left]

                # select random index
                pivot_index = random.randint(left,right)
                #  find the pivot in its final location
                pivot_index = partition(left,right,pivot_index)

                # the pivot is in its final sorted position
                if k_smallest == pivot_index:
                    return A[k_smallest]
                elif k_smallest < pivot_index:
                    return select(left,pivot_index-1,k_smallest)
                else:
                    return select(pivot_index+1,right,k_smallest)

            # kth largest is (n-k)th smallest
            return select(0,len(A)-1,len(A)-k)
    # Time complexity : O(Nlogk). N to loop through the elements and
    # log k for insertion deletion of items in heap
    # Space complexity : O(k) to store the heap elements.
    def findK_heap(self, A:List[int],k:int) -> int:
        return heapq.nlargest(k, A)[-1]


if __name__ == "__main__":
    mySolution = Solution()

    print("pivot - forth largest number is: ",mySolution.findkthLargest([1,2,3,4,5,22,23,55,65,3],4))
    print("heap - forth largest number is: ",mySolution.findK_heap([1,2,3,4,5,22,23,55,65,3],4))

    # pivot - forth largest number is:  22
    # heap - forth largest number is:  22

    print("pivot - forth largest number is: ",mySolution.findkthLargest([3,2,1,5,6,4],2))
