from typing import List

class Solution:
    def car_fleet(self,target: int, position:List[int],speed: List[int])-> int:

        fleets =[]
        # merge items
        for i in range(len(position)):
            fleets.append([position[i],speed[i]])
        # sort on position person closes to finish at the right
        fleets.sort()
        finish_times = []

        # calculate finish time
        # finish time = (number of slots needed to finish) * speed
        # number of slots needed = target minus fleet[i]
        for i in range(len(fleets)):
            finish_times.append(((target-fleets[i][0]) * fleets[i][1]))

        # loop through items if previous time is earlier than current then add one to fleet this means its a new fleet
        previous_finish = 0
        # our result
        number_fleets = 0
        for i in range(len(finish_times)-1,-1,-1):
            if finish_times[i] > previous_finish:
                number_fleets+= 1
                previous_finish = finish_times[i]


        return number_fleets




if __name__ =="__main__":
    mySolution = Solution()
    print(mySolution.car_fleet(12,[10,8,0,5,3],[2,4,1,1,3]))
