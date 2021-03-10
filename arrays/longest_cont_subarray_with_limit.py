
from typing import List
import collections

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # monotonically increasing and decresig queue
        # these queue incrase from left to right in the queue
        # similarly the queue decreases from left to right in the queue
        maxd = collections.deque()
        mind = collections.deque()
        i = 0
        for a in nums:
            # loop through max queue if a is greater than the max of the queue
            # pop until a and fix the right side of queue
            print("Max queue:",maxd," adding: ",a)
            while len(maxd) and a > maxd[-1]: maxd.pop()
            # loop through to maintain the montonically drecreasing order
            while len(mind) and a < mind[-1]: mind.pop()
            print("Max queue with right side fixed up:",maxd)
            # now that the queues are fixed up add current number to its location in each queue
            maxd.append(a)
            mind.append(a)
            print("add current number to max queue:",maxd)
            # now fix the right side of the queue
            if maxd[0] - mind[0] > limit:
                if maxd[0] == nums[i]: maxd.popleft()
                if mind[0] == nums[i]: mind.popleft()
                i += 1
            print("fix up left side of max queue:",maxd)
            print("")
        return len(nums) - i


if __name__=="__main__":
    mySolution = Solution()
    arr = [10,1,2,4,7,2,2,2,5,4,12,1,2,3]
    arr2 = [8,2,4,7]
    limit = 5
    limit2 = 4
    print(mySolution.longestSubarray(arr,limit))
    # print(mySolution.longestSubarray(arr2,limit2))
