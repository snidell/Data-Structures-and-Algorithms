# 13.8 Compute the Union of Intervals
# Design an algorithm that takes as input a set of intervals, and outputs their
# union expressed as a set of disjoint intervals.
# Hint: Do a case analysis.

import collections
from typing import List
Endpoint = collections.namedtuple('Endpoint',('is_closed','val'))
Interval = collections.namedtuple('Interval',('left','right'))


class Solution:
    def add_interval(self,intervals: List[Interval]) -> List[Interval]:
        #Empty input.
        if not intervals:
            return []

        def is_mergable(i1,i2):
            # if the current left value is lower than max right
            return (i1.left.val < i2.right.val or
                    # or they are equal and either are closed
                        (i1.left.val == i2.right.val and
                        (i1.left.is_closed or i2.right.is_closed)))


        def right_updateable(i1,i2):
            # if the current right is greater than max right update
            return (i1.right.val > i2.right.val or
                # or if they are equal and current is closed update
                (i1.right.val == i2.right.val and i1.right.is_closed))


        # Sort intervals according to left endpoints of intervals.
        intervals.sort(key=lambda i: (i.left.val, not i.left.is_closed))
        # load the first interval in so we have something to compare
        # this is the lowest interval since we sorted it
        result = [intervals[0]]
        for i in intervals:
            if intervals and is_mergable(i,result[-1]):
                if right_updateable(i,result[-1]):
                    result[-1] = Interval(result[-1].left, i.right)
            else: result.append(i)
        return result


if __name__ =="__main__":
    mySolution = Solution()
    myIntervals = []
    e1 = Endpoint(True,1)
    i1 = Interval(e1,e1)
    myIntervals.append(i1)

    e2 = Endpoint(False,0)
    e3 = Endpoint(False,3)
    i2 = Interval(e2,e3)
    myIntervals.append(i2)

    e4 = Endpoint(True,2)
    e5 = Endpoint(True,4)
    i3 = Interval(e4,e5)
    myIntervals.append(i3)

    e6 = Endpoint(True,3)
    e7 = Endpoint(False,4)
    i4 = Interval(e6,e7)
    myIntervals.append(i4)

    e8 = Endpoint(True,5)
    e9 = Endpoint(False,7)
    i5 = Interval(e8,e9)
    myIntervals.append(i5)

    e10 = Endpoint(True,7)
    e11 = Endpoint(False,8)
    i6 = Interval(e10,e11)
    myIntervals.append(i6)

    e12 = Endpoint(True,8)
    e13 = Endpoint(False,11)
    i7 = Interval(e12,e13)
    myIntervals.append(i7)

    e14 = Endpoint(False,9)
    e15 = Endpoint(True,11)
    i8 = Interval(e14,e15)
    myIntervals.append(i8)

    e16 = Endpoint(True,12)
    e17 = Endpoint(True,14)
    i9 = Interval(e16,e17)
    myIntervals.append(i9)

    e18 = Endpoint(False,12)
    e19 = Endpoint(True,16)
    i10 = Interval(e18,e19)
    myIntervals.append(i10)

    e20 = Endpoint(False,16)
    e21 = Endpoint(False,17)
    i11 = Interval(e20,e21)
    myIntervals.append(i11)




    print(mySolution.add_interval(myIntervals))
