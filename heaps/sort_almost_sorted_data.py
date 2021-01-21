# 10.3 SORT AN ALMOST-SORTED ARRAY
# Often data is almost-sorted-for example, a server receives timestamped stock
# quotes and earlier quotes may arrive slightly after later quotes because of
# differences in server loads and network routes. In this problem we address
# efficient ways to sort such data.
#
# Write a program which takes as input a very long sequence of numbers and prints
# the numbers in sorted order. Each number is at most k away from its correctly
# sorted position. (Such an array is sometimes referred to as being k-sorted.)
# For example, no number in the sequence (3, -1, 2, 6, 4, 5, 8) is more
# than 2 away from its final sorted position.
#
# Hint: How many numbers must you read after reading the ith number to be sure
# you can place it in the correct location?
from typing import List
from typing import Iterator
import itertools
import heapq

class Solution:
    def sort_almost_sorted(self,sequence: Iterator[int], k: int) -> List[int]:
        result = []
        #  create min heap
        min_heap: List[int] = []
        #  initialize heap loop until you have k+1 items in heap
        for x in itertools.islice(sequence,k):
            heapq.heappush(min_heap,x)

        #  once reached k+1 pop smallet entry and add next i
        for x in sequence:
            smallest = heapq.heappushpop(min_heap,x)
            result.append(smallest)

        # now ensure the heap is empty as it will have some remaining items
        while min_heap:
            result.append(heapq.heappop(min_heap))

        return result



if __name__ == "__main__":
    mySolution = Solution()
    myIt = iter([3, -1, 2, 6, 4, 5, 8])
    print(mySolution.sort_almost_sorted(myIt,2))
