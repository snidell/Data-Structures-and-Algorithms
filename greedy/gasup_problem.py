# 17.6 The GASUP PROBLEM


# In the gasup problem, a number of cities are arranged on a circular road. You
# need to visit all the cities and come back to the starting city. A certain
# amount of gas is available at each city. The amount of gas summed up over all
# cities is equal to the amow1t of gas required to go around the road once. Your
# gas tank has unlimited capacity. Call a city ample if you can begin at that
# city with an empty tank, refill at it, then travel through all the remaining
# cities, refilling at each, and return to the ample city, without running out
# of gas at any point. See Figure 17.2 on the following page for an example.

# Given an instance of the gasup problem, how would you efficiently compute an
# ample city? You can assume that there exists an ample city. The input is given
# in the form of two arrays-one for the amount of gas at each city, the other for
# the distance to the next city. For the example in Figure 17.2 on the next page,
# these arrays are (50, 20, 5, 30, 25, 10, 10), and
# (900, 600, 200,400, 600, 200, 100). (For this example, there is only one
# ample city, namely D.)

# Leetcode 134 Gas Station https://leetcode.com/problems/gas-station/

import collections
from typing import List

class Solution:
    MPG = 20
    # gallons[i] is the amount of gas and city i, distance[i] is the distance
    # to the next city

    def find_ample_city(self,gallons:List[int],distances:List[int])->int:
        remaining_gallons = 0
        CityAndRemainingGas = collections.namedtuple('CityAndRemainingGas',
                                            ('city','remaining_gallons'))

        city_remaining_gas_pair = CityAndRemainingGas(0,0)
        num_cities = len(gallons)

        for i in range(1,num_cities):
            remaining_gallons += gallons[i-1] - distances[i-1] // self.MPG
            if remaining_gallons < city_remaining_gas_pair.remaining_gallons:
                city_remaining_gas_pair = CityAndRemainingGas(
                    i,remaining_gallons)
        return city_remaining_gas_pair.city

    # Leetcode implementation
    # TIme O(n)
    # Space O(1)
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)

        total_tank, curr_tank = 0, 0
        starting_station = 0
        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            # If one couldn't get here,
            if curr_tank < 0:
                # Pick up the next station as the starting one.
                starting_station = i + 1
                # Start with an empty tank.
                curr_tank = 0

        return starting_station if total_tank >= 0 else -1

if __name__ =="__main__":
    mySolution = Solution()
    gallons = [50,20,5,30,25,10,10]
    city = [900,600,200,400,600,200,100]
    print(mySolution.find_ample_city(gallons,city))
    # Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
    # Output: 3
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    print(mySolution.canCompleteCircuit(gas,cost))
