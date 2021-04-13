# Leetcode 853 Car Fleet
# N cars are going to the same destination along a one lane road.  The
# destination is target miles away.
#
# Each car i has a constant speed speed[i] (in miles per hour), and initial
# position position[i] miles towards the target along the road.
#
# A car can never pass another car ahead of it, but it can catch up to it, and
# drive bumper to bumper at the same speed.
#
# The distance between these two cars is ignored - they are assumed to have the
# same position.
#
# A car fleet is some non-empty set of cars driving at the same position and
# same speed.  Note that a single car is also a car fleet.
#
# If a car catches up to a car fleet right at the destination point, it will
# still be considered as one car fleet.
#
#
# How many car fleets will arrive at the destination?
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int],speed:List[int])-> int:
        cars = sorted(zip(position, speed))
        times =[]
        for pos, speed in cars:
            # calculate finishing times
            times.append(float(target-pos)/speed)
        ans = 0
        while len(times) > 1:
            lead = times.pop()
            print(lead,times[-1])
            if lead < times[-1]:
                # if lead arrives sooner, it can't be caught
                ans += 1
            else:
                # else, fleet arrives at later time 'lead'
                times[-1] = lead
        # remaining car is fleet (if it exists)
        print(times)
        return ans + bool(times)





if __name__ =="__main__":
    mySolution = Solution()
    # 0 5 3 8 10      1,8,4
    # 1 3 1 4 2

    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    target = 12

    # position = [3]
    # speed = [3]
    # target = 10

    # position = [8,3,7,4,6,5]
    # speed = [4,4,4,4,4,4]
    # target = 10
    # ans = 6
    print(mySolution.carFleet(target,position,speed))
