# Leetcode 253. Meeting Rooms II
# Given an array of meeting time intervals intervals where intervals[i] =
# [starti, endi], return the minimum number of conference rooms required.

# Example 1:
#
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Example 2:
#
# Input: intervals = [[7,10],[2,4]]
# Output: 1

from typing import List
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        # a min heap that describes the meeting rooms, sorted by the end time
        meeting_rooms = []
        max_num_rooms = 0
        for meeting in intervals:
            # while the meeting that has an ending time sooner than the new meetings start time

            while meeting_rooms and meeting_rooms[0] < meeting[0]:
                heapq.heappop(meeting_rooms)

            # add new meeting
            heapq.heappush(meeting_rooms,meeting[1])
            max_num_rooms = max(max_num_rooms,len(meeting_rooms))
        return max_num_rooms


if __name__ =="__main__":
    mySolution = Solution()
    meetings = [[0,30],[5,10],[15,20]]
    print(mySolution.minMeetingRooms(meetings))
