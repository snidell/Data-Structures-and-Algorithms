# 13.6 RENDER A CALENDAR
# Write a program that takes a set of events, and determines the maximum number
# of events that take place concurrently.

from typing import List
import collections

Event = collections.namedtuple('Event' , ('start' , 'finish'))

class Solution:
    # time complexity sorting give n(Log(N)) time and iterating through
    # E give O(N) reduces to N(log(N))
    # Space complexity we use an addiitonal DS the size of n so O(N)
    def find_concurrent_events(self,A:List[Event])-> int:
        # Endpoint is a tuple (start_time, 0) or (end_time, 1) so that if times
        # are equal start_time comes first

        Endpoint = collections.namedtuple('Endpoint',('time','is_start'))

        E =[]
        # build array of all endpoints
        for event in A:
            E.append(Endpoint(event.start,True))
            E.append(Endpoint(event.finish,False))

        # first sort on time then if its start/end
        E.sort(key=lambda e: (e.time, not e.is_start))
        # E sorted by time first then start> finish second
        # [Endpoint(time=1, is_start=True), Endpoint(time=2, is_start=True),
        # Endpoint(time=4, is_start=True), Endpoint(time=5, is_start=False),
        # Endpoint(time=5, is_start=False), Endpoint(time=6, is_start=True),
        # Endpoint(time=7, is_start=False), Endpoint(time=8, is_start=True),
        # Endpoint(time=9, is_start=True), Endpoint(time=9, is_start=False),
        # Endpoint(time=10, is_start=False), Endpoint(time=11, is_start=True),
        # Endpoint(time=12, is_start=True), Endpoint(time=13, is_start=False),
        # Endpoint(time=14, is_start=True), Endpoint(time=15, is_start=False),
        # Endpoint(time=15, is_start=False), Endpoint(time=17, is_start=False)]

        # track the number of simultaneous events
        max_events, num_events = 0,0

        # now the data is structured with time then starts first add 1 to
        # max_events if its a start and - if its a finish

        for e in E:
            if e.is_start:
                num_events += 1
                max_events = max(max_events,num_events)
            else:
                num_events -= 1
        return max_events



if __name__ =="__main__":
    mySolution = Solution()
    event1 = Event(1,5)
    event2 = Event(6,10)
    event3 = Event(11,13)
    event4 = Event(14,15)
    event5 = Event(2,7)
    event6 = Event(8,9)
    event7 = Event(12,15)
    event8 = Event(4,5)
    event9 = Event(9,17)
    A = [event1,event2,event3,event4,event5,event6,event7,event8,event9]
    print(mySolution.find_concurrent_events(A))
