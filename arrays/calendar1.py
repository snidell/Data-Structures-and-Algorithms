# https://leetcode.com/problems/my-calendar-i/
# Implement a MyCalendar class to store your events. A new event can be added if
# adding the event will not cause a double booking.
#
# Your class will have the method, book(int start, int end). Formally, this
# represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.
#
# A double booking happens when two events have some non-empty intersection
# (ie., there is some time that is common to both events.)
#
# For each call to the method MyCalendar.book, return true if the event can be
# added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
#
# Your class will be called like this: MyCalendar cal = new MyCalendar();
# MyCalendar.book(start, end)
#
# Example 1:
#
# MyCalendar();
# MyCalendar.book(10, 20); // returns true
# MyCalendar.book(15, 25); // returns false
# MyCalendar.book(20, 30); // returns true
# Explanation:
# The first event can be booked.  The second can't because time 15 is already booked by another event.
# The third event can be booked, as the first event takes every time less than 20, but not including 20.

from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        # add -INF/INF to the head and the end to make it easy to check leftmost and rightmost boundary
        self.cal = SortedList([(float('-inf'),float('-inf')),(float('inf'),float('inf'))])

    def book(self, start: int, end: int) -> bool:
        interval = (start, end)
        # either bisect(bisect_right)/bisect_left works
        i = self.cal.bisect(interval)
        print(interval)
        print(self.cal)
        print("i:",i)
        if self.cal[i-1][1] <= start and end <= self.cal[i][0]:
            self.cal.add(interval)
            return True


        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

if __name__ =="__main__":
    cal = MyCalendar()
    cal.book(5, 10)
    cal.book(10, 20) # true
    cal.book(15, 25) # false
    cal.book(20, 30) # true
    cal.book(40, 42)
    cal.book(33, 35)
    cal.book(1, 200)

# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# [[0, 1, 1, 1], [1, 1, 2, 2], [0, 1, 2, 3]]
 dp=[]
        for i in range(len(matrix)):
            dp.append([0]*len(matrix[0]))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i==0 or j==0:
                    dp[i][j]=matrix[i][j]
                elif matrix[i][j]==0:
                    dp[i][j]=0
                elif matrix[i][j]==1:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        Sum=0
        for i in range(len(dp)):
            Sum=Sum+sum(dp[i])
        return Sum


# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# [[0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 2, 2]]
# create 2d matrix to store dp cache
