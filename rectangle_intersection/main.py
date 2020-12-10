import collections
Rect = collections.namedtuple('Rect',('x','y','width','height'))
class Solution:
    def intersect_rectangle(self, r1:Rect,r2:Rect)->Rect:
        def is_intersect(r1,r2):
            # r1.x<=r2.x + r2.width ==> check if r1 within r2s range
            # r1.x +r1.width >= r2.x ==>
            return (r1.x<=r2.x + r2.width and r1.x +r1.width >= r2.x
                    and r1.y <=r2.y +r2.height and r1.y + r1.height >=r2.y)

        if not is_intersect(r1,r2):
            return Rect(0,0,-1,-1)
        return Rect(max(r1.x,r2.x),max(r1.y,r2.y),
                    min(r1.x+r1.width,r2.x+r2.width)-max(r1.x,r2.x),
                    min(r1.y+r1.height,r2.y+r2.height)-max(r1.y,r2.y))


if __name__=="__main__":
    mySolution = Solution()
    r1 = Rect(0,0,2,2)
    r2 = Rect(2,2,2,2)
    print(mySolution.intersect_rectangle(r1,r2))
    r3 = Rect(3,3,2,2)
    print(mySolution.intersect_rectangle(r1,r3))
    r4 = Rect(-1,-1,2,2)
    print(mySolution.intersect_rectangle(r1,r4))
