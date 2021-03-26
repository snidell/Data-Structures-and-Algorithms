# 528. Random Pick with Weight
# You are given an array of positive integers w where w[i] describes the weight
# of ith index (0-indexed).
#
# We need to call the function pickIndex() which randomly returns an integer in
# the range [0, w.length - 1]. pickIndex() should return the integer proportional
# to its weight in the w array. For example, for w = [1, 3], the probability of
# picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of
# picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).
#
# More formally, the probability of picking index i is w[i] / sum(w).

from typing import List
import random
import bisect

class Solution:
    def __init__(self, w: List[int]):
        """
        :type w: List[int]
        """
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        # prefix_sums = [1,4,9,16]
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        """
        :rtype: int
        """
        # get random target
        target = self.total_sum * random.random()
        # run a binary search to find the target zone
        interval_idx = bisect.bisect(self.prefix_sums, target)
        return interval_idx
        # print(interval_idx)
        # low, high = 0, len(self.prefix_sums)
        # while low < high:
        #     mid = low + (high - low) // 2
        #     if target > self.prefix_sums[mid]:
        #         low = mid + 1
        #     else:
        #         high = mid
        # # since the majority of the span will be further to the right, this is the most liekly to be chosen
        # return low


if __name__=="__main__":
    mySolution = Solution([1,3,5,7])
    print(mySolution.pickIndex())
