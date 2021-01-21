# 10.1 MERGE SORTED FILES
# This problem is motivated by the following scenario. You are given 500 files, e
# ach containing stock trade information for an S&P 500 company. Each trade is
# encoded by a line in the following format: 1232111,AAPL,3©,456.12.
# Write a program that takes as input a set of sorted sequences and computes
# the union of these sequences as a sorted sequence. For example, if the input is
# (3, 5, 7), (0, 6), and (0, 6, 28), then the output is (0, 0,3, 5, 6, 6, 7, 28).


# Youtube walkthrough : https://www.youtube.com/watch?v=6bvnZzwiKzs

from typing import List
import heapq

class Solution:
    def merge_sorted_arrays(self,sorted_arrays: [List[int]])->List[int]:
        min_heap: List[Tuple[int][int]] = []
        sorted_arrays_iters = [iter(x) for x in sorted_arrays]

        # initalize heap by putting first element of each array into heap
        for i ,it in enumerate(sorted_arrays_iters):
            first_element = next(it,None)
            #  check for length of zero array here
            if first_element is not None:
                heapq.heappush(min_heap,(first_element,i))

        # build result
        result = []
        while min_heap:
            smallest_entry , smallest_array_i = heapq.heappop(min_heap)
            smallest_array_iter = sorted_arrays_iters[smallest_array_i]
            result.append(smallest_entry)
            next_element = next(smallest_array_iter,None)
            if next_element is not None:
                heapq.heappush(min_heap,(next_element,smallest_array_i))

        return result

if __name__ == "__main__":
    mySolution = Solution()
    print(mySolution.merge_sorted_arrays([[1,2,3],[-22,5,6],[-1,8,9]]))
    first , last  = range(2)
    print(first)
    print(last)

    myString = "OneTwoThree"
    inter = myString[::-1]
    print(inter[::-1])
    # result [-22, -1, 1, 2, 3, 5, 6, 8, 9]


    # Let le be the number of input sequences. Then there are no more than k
    # elements in the min-heap. Both extract-min and insert take O(log k) time.
    # Hence, we can do the merge in O(n logic) time. The space complexity
    # is O(k) beyond the space needed to write the final result. In particular,
    # if the data comes from files and is written to a file, instead of arrays,
    # we would need only O(k) additional storage.
