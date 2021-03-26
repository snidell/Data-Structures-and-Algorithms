# 57. Insert Interval

# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
#
# You may assume that the intervals were initially sorted according to their
# start times.
#
# Example 1:
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
# Example 3:
#
# Input: intervals = [], newInterval = [5,7]
# Output: [[5,7]]

from typing import List
import bisect

class Solution:
    # Time complexity is O(N) could insert the first item
    # Space O(n)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def merge_interval(int1,int2):
            start = min(int1[0],int2[0])
            end = max(int1[1],int2[1])
            print(start,end)
            return [start,end]

        idx,n = 0 , len(intervals)
        result = []
        while idx < n and intervals[idx][0] < newInterval[0]:
            result.append(intervals[idx])
            idx+=1

        if result and result[-1][1] >= newInterval[0]:
            result[-1] = merge_interval(result[-1],newInterval)
        else:
            result.append(newInterval)

        while idx < n:
            if intervals[idx][0] <= result[-1][1]:
                print("call")
                result[-1] = merge_interval(intervals[idx],result[-1])
            else:
                result.append(intervals[idx])
            idx+=1

        return result



if __name__ =="__main__":
    mySolution = Solution()
    # intervals = [[1,3],[6,9]]
    # new_interval = [2,5]
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    new_interval = [4,8]
    print(mySolution.insert(intervals,new_interval))
