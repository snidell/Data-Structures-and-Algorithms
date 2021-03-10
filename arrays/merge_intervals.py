# Given an array of intervals where intervals[i] = [starti, endi], merge all
# overlapping intervals, and return an array of the non-overlapping intervals
# that cover all the intervals in the input.
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

from typing import List
class Solution:
    def merge(self,intervals: List[List[int]])->List[List[int]]:
        def merge_intervals(int1,int2):
            return [min(int1[0],int2[0]),max(int1[1],int2[1])]

        intervals.sort()
        results = []
        results.append(intervals[0])

        for i in range(1,len(intervals)):
            print(results[-1][1],intervals[i][0])
            if results[-1][1] >= intervals[i][0]:
                results[-1] = merge_intervals(results[-1],intervals[i])
            else:
                results.append(intervals[i])
        return results



if __name__ =="__main__":
    mySolution = Solution()
    print(mySolution.merge([[1,4],[0,2],[3,5]]))






















   # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
   #      intervals.sort()
   #      result = []
   #      def merge_interval(interval1: List[int],interval2: List[int]):
   #          return [min(interval1[0],interval2[0]),max(interval1[1],interval2[1])]
   #
   #
   #      for i,interval in enumerate(intervals):
   #          if i == 0:
   #              result.append(interval)
   #
   #          most_recent_interval = result[-1]
   #           # is the lowest bound is below upper bound of previous
   #          if most_recent_interval[1] >= interval[0]:
   #              result[-1] = merge_interval(most_recent_interval,interval)
   #          else:
   #              # intervals do not overlap so add new interval
   #              result.append(interval)
   #
   #
   #
   #      return result
