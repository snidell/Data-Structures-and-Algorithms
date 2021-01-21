# 10.4 COMPUTE THE k-CLOSEST STARS
#
# Consider a coordinate system for the Milky Way, in which Earth is at (0,0, 0).
# Model stars as points, and assume distances are in light years. The Milky Way
# consists of approximately 1012 stars, and their coordinates are stored in a
# file. How would you compute the k stars which are closest to Earth?
#
# Hint: Suppose you know the k closest stars in the first n stars. If the
# (n + l)th star is to be added to
# the set of k closest stars, which element in that set should be evicted?
from typing import List
from typing import Iterator
import heapq
import math

class Star:
    def __init__(self, x: int, y: int, z:int, name:str):
        self.x, self.y,self.z = x,y,z
        self.name = name
    @property
    def distance(self)-> float:
        return math.sqrt(self.x**2+self.y**2+self.z**2)

    # magic method to compare Stars less than == lt
    def __lt__(self,rhs: 'Star')-> bool:
        return self.distance < rhs.distance

def find_closest_k_stars(stars: Iterator[Star], k:int)-> List[Star]:
    max_heap: List[Tuple[float,Star]] = []
    for star in stars:
        heapq.heappush(max_heap,(-star.distance, star))
        if len(max_heap) == k+1:
            heapq.heappop(max_heap)


    return [s[1] for s in heapq.nlargest(k,max_heap)]


if __name__ =="__main__":
    myStar1 = Star(0,0,0,"Earth")
    myStar2 = Star(2,2,2,"Mars")
    myStar3 = Star(1,1,1,"Moon")
    myStar4 = Star(20,21,26,"Pluto")
    myStar5 = Star(15,12,13,"Saturn")
    myStar6 = Star(4,5,5,"Mercury")
    myStar7 = Star(6,6,7,"Sun")
    myStar8 = Star(17,15,20,"Neptune")

    stuff = []
    stuff.append(myStar2)
    stuff.append(myStar3)
    stuff.append(myStar4)
    stuff.append(myStar5)
    stuff.append(myStar6)
    stuff.append(myStar7)
    stuff.append(myStar8)
    myIt = iter(stuff)
    result = find_closest_k_stars(myIt,4)

    for star in result:
        print(star.name+" ",star.distance)
