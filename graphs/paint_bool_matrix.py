# 18.2 PAINT A BOOLEAN MATRIX

import collections
from typing import List

class Solution:
    # time complexity O(mn) we could possibly go the whole board
    # space complexity is O(m+n) 
    def flip_color(self,x:int,y:int, image:List[List[bool]])-> None:
        color = image[x][y]
        # setup queue for BFS
        q = collections.deque([(x,y)])
        # flip the initial index color
        image[x][y] = not image[x][y]

        # start BFS
        while q:
            x,y, = q.popleft()
            # go right, left, up and down
            for next_x,next_y in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                # check if your inbounds
                if (0 <= next_x < len(image) and 0<= next_y < len(image[next_x])
                    and image[next_x][next_y] == color):
                    # flip color do some action with BFS
                    image[next_x][next_y] = not image[next_x][next_y]
                    q.append((next_x,next_y))



if __name__ =="__main__":
    mySolution = Solution()
    image =[
        [True,False,False,False,False,False,True,True,False,False],
        [True,False,False,False,False,False,True,True,False,False],
        [True,False,False,False,False,False,True,True,False,False],
        [True,False,False,False,False,False,True,True,False,False],
        [True,False,False,False,False,False,True,True,False,False],
        [True,False,False,False,False,False,True,True,False,False],
        [True,False,False,False,False,False,True,True,False,False],
        [True,False,False,False,False,False,True,True,False,False],
        [True,False,False,False,False,False,True,True,False,False],
        [True,False,False,False,False,False,True,True,False,False],
        [True,False,False,False,False,False,True,True,False,False],
        [True,False,False,False,False,False,True,True,False,False],
    ]
    print(image)
    mySolution.flip_color(3,1,image)
    print(image)
