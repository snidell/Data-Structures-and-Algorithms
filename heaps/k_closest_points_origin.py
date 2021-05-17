# 973. K Closest Points to Origin
# Given an array of points where points[i] = [xi, yi] represents a point on the
# X-Y plane and an integer k, return the k closest points to the origin (0, 0).
#
# The distance between two points on the X-Y plane is the Euclidean distance
# (i.e., √(x1 - x2)2 + (y1 - y2)2).
#
# You may return the answer in any order. The answer is guaranteed to be unique
# (except for the order that it is in).

from typing import List
import heapq
class Solution:
    def kClosest(self,points:List[List[int]], k:int)-> List[int]:
        heap = []

        for (x, y) in points:
            dist = -(x*x + y*y)
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        print(heap)
        return [(x,y) for (dist,x, y) in heap]



if __name__ =="__main__":
    stuff =[[3,3],[5,-1],[-2,4],[1,0],[0,0]]
    mySolution = Solution()
    print(mySolution.kClosest(stuff,1))
