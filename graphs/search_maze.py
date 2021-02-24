import collections
from typing import List
WHITE,BLACK = range(2) # white = 0 Black = 1
Coordinate = collections.namedtuple('Coordinate',('x','y'))

class Solution:
    def search_maze(self,maze:List[List[int]],s:Coordinate,
                    e:Coordinate)-> List[Coordinate]:

        def search_maze_helper(cur):
            # check cur is within maze and is a white pixel
            if not(0<= cur.x < len(maze) and 0 <= cur.y < len(maze[cur.x]) and maze[cur.x][cur.y] == WHITE):
                return False

            path.append(cur)
            maze[cur.x][cur.y] = BLACK
            if cur == e:
                print("endpoint",e)
                return True

            # proceed with depth first search. go left, go right go down go up
            if (search_maze_helper(Coordinate(cur.x - 1,cur.y)) or
            search_maze_helper(Coordinate(cur.x + 1,cur.y)) or
            search_maze_helper(Coordinate(cur.x,cur.y - 1)) or
            search_maze_helper(Coordinate(cur.x,cur.y + 1))):
                return True

        path: List[Coordinate] = []
        search_maze_helper(s)
        return path

if __name__ =="__main__":
    mySolution = Solution()
    maze = [[1,0,0,0,0,0,1,1,0,0],
            [0,0,1,0,0,0,0,0,0,0],
            [1,0,1,0,0,1,1,0,1,1],
            [0,0,0,1,1,1,0,0,1,0],
            [0,1,1,0,0,0,0,0,0,0],
            [0,1,1,0,0,1,0,1,1,0],
            [0,0,0,0,1,0,0,0,0,0],
            [1,0,1,0,1,0,1,0,0,0],
            [1,0,1,1,0,0,0,1,1,1],
            [0,0,0,0,0,0,0,1,1,0],
    ]
    start = Coordinate(9,0)
    end = Coordinate(0,9)
    print(mySolution.search_maze(maze,start,end))
