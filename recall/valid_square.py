
from typing import List
import math
class Solution:
    def valid_square(self,p1:List[int],p2:List[int],p3:List[int],p4:List[int])-> bool:
        # first define the distance formula between two points

        def distance(x,y):
            return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

        # now that we have the distance lets get the distance between all points

        distances = [distance(p1,p2),distance(p1,p3),distance(p1,p4),distance(p2,p3),distance(p2,p4),distance(p3,p4)]
        distances.sort()
        print(distances)
        # are the sides the same length ?
        if distances[0] == distances[1] == distances[2] == distances[3]:
            # are the diagonals the same length ?
            if distances[4] == distances[5]:
                return True

        return False






if __name__ =="__main__":
    mySolution = Solution()
    points = [[0,0],[0,1],[1,1],[1,0]]
    print(mySolution.valid_square(points[0],points[1],points[2],points[3]))
