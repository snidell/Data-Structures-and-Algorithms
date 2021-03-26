# 10.5 COMPUTE THE MEDIAN OF ONLINE DATA
#
# You want to compute the running median of a sequence of numbers. The sequence
# is presented to you in a streaming fashion-you cannot back up to read an
# earlier value, and you need to output the median after reading in each
# new element. For example, if the input is 1, 0, 3, 5,2, 0, 1 the output
# is 1,0.5, 1,2,2, 1.5, 1.
#
# Design an algorithm for computing the running median of a sequence.
# Hint: Avoid looking at all values each time you read a new value.

from typing import List
from typing import Iterator
import heapq

class Solution:
    def get_median(self,sequence: Iterator[int])-> List[float]:
        #  stores large half
        min_heap: List[int] = []
        # stores smaller half
        max_heap: List[int] = []

        result = []
        for x in sequence:
            # push ontop max heap while maintainging both min/max heaps
            heapq.heappush(max_heap,-heapq.heappushpop(min_heap,x))
            # ensure each heap has same num elements or min heap has +1 more
            
            if len(max_heap) > len(min_heap):
                heapq.heappush(min_heap,-heapq.heappop(max_heap))
            print("max_heap: ",max_heap," min_heap: ",min_heap)
            result.append(0.5 * (min_heap[0] + (-max_heap[0])) if len(min_heap)
                           ==  len(max_heap) else min_heap[0])

        return result


if __name__ == "__main__":
    mySolution = Solution()
    myIt = iter([3, -1, 2, 6, 4, 5, 8])

    # result of the runnign median : [3, 1.0, 2, 2.5, 3, 3.5, 4]

    print(mySolution.get_median(myIt))

    myList = [1,1,2,3,4,4,5,6,6,7,8]

    # mySet = set(myList)
    # for num in mySet:
    #     print(num)
    #
    # myRanList = [1,34,344,33,5,56,7,8,9,10,11]
    # heapq.heapify(myRanList)
    # print("heap list: ",myRanList)
    # print(heapq.heappop(myRanList))
    # print("heap list: ",myRanList)
    # print(heapq.heappop(myRanList))
    # print("heap list: ",myRanList)
    # print(heapq.heappop(myRanList))
    # print("heap list: ",myRanList)
    # print(heapq.heappop(myRanList))
    # print("heap list: ",myRanList)
    # print(heapq.heappop(myRanList))
    # print("heap list: ",myRanList)
    # print(heapq.heappop(myRanList))
    # print("heap list: ",myRanList)
    # print(heapq.heappop(myRanList))
    # print("heap list: ",myRanList)
