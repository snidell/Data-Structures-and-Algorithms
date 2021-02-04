# interview with MongoDB 1/28/2021
# Leetcode 56 Merge intervals
# Book quesiton 13.7 Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi],
# merge all overlapping intervals, and return an array of the non-overlapping
# intervals that cover all the intervals in the input.
from typing import List
class Solution:
    def merge(self,intervals: List[List[int]])-> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        print(intervals)
        result = []
        def merge_interval(interval1: List[int],interval2: List[int]):
            return [min(interval1[0],interval2[0]),max(interval1[1],interval2[1])]
        def get_span(interval:List[int]) -> int:
            return interval[1] - interval[0]


        for i,interval in enumerate(intervals):
            if i == 0:
                result.append(interval)

            most_recent_interval = result[-1]
             # is the lowest bound is below upper bound of previous
            if most_recent_interval[1] >= interval[0]:
                result[-1] = merge_interval(most_recent_interval,interval)
            else:
                # intervals do not overlap so add new interval
                result.append(interval)

        # add up the spans of the intervals
        total = 0
        for interval in result:
            total+= get_span(interval)

        return result

if __name__ =="__main__":
    mySolution = Solution()
    print(mySolution.merge([[1,2],[1,1],[2,12],[3,4],[6,8]]))
