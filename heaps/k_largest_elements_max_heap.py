from typing import List
import heapq

class Solution:
    def k_largest_in_max_heap(self,A: List[int],k:int)-> List[int]:
        if k<= 0:
            return []

        candidate_max_heap = []
        candidate_max_heap.append((-A[0],0))
        result = []
        for _ in range(k):
            candidate_idx = candidate_max_heap[0][1]
            result.append(-heapq.heappop(candidate_max_heap)[0])

            left_child_idx = 2 * candidate_idx + 1
            if left_child_idx < len(A):
                heapq.heappush(candidate_max_heap,(-A[left_child_idx],left_child_idx))

            rigth_child_idx = 2 * candidate_idx + 2
            if rigth_child_idx < len(A):
                heapq.heappush(candidate_max_heap,(-A[rigth_child_idx],rigth_child_idx))

        return result


if __name__ == "__main__":
    mySolution = Solution()

    listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    heapq._heapify_max(listForTree)
    print(listForTree)
    print(mySolution.k_largest_in_max_heap(listForTree,6))
