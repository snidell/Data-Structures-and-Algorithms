from sortedcontainers import SortedDict
class RangeModule:

    def __init__(self):
        self.data = SortedDict()

    def addRange(self, left: int, right: int) -> None:
        l, r = self.data.bisect(left), self.data.bisect(right)
        if l != 0:
            # move L to the left by 1 this will point to the lower bound
            l -= 1
            # if the left is larger than the previous interval we need to move it up
            if self.data.peekitem(l)[1] < left:
                l += 1
        if l != r:
            # given the adjust left and right intervals we need to check if a merge needs to happen. we take
            # the min of the left intervals and the max of the right intervals to maximize the interval size.
            left, right = min(left, self.data.peekitem(l)[0]), max(right, self.data.peekitem(r-1)[1])
            # now that we have the new interval we need ot pop the redundant intervals
            for _ in range(l, r):
                self.data.popitem(l)
        # insert the new interval
        self.data[left] = right
        print(self.data)

    def queryRange(self, left: int, right: int) -> bool:
        l, r = self.data.bisect_right(left), self.data.bisect_right(right)
        print("l == 0: ",(l == 0), "self.data.peekitem(l-1)[1] < right: ",(self.data.peekitem(l-1)[1] < right))
        if l == 0 or self.data.peekitem(l-1)[1] < right: return False

        return True

    def removeRange(self, left: int, right: int) -> None:
        l, r = self.data.bisect_right(left), self.data.bisect_right(right)
        if l != 0:
            l -= 1
            if self.data.peekitem(l)[1] < left:
                l += 1
        if l != r:
            ll, rr = min(left, self.data.peekitem(l)[0]), max(right, self.data.peekitem(r-1)[1])
            for _ in range(l, r):
                self.data.popitem(l)
            if ll < left: self.data[ll] = left
            if right < rr: self.data[right] = rr


if __name__ =="__main__":
    myRM = RangeModule()
    print("---adding first interval")
    myRM.addRange(10, 20) # initial range
    print("---adding second interval")
    myRM.addRange(5, 7) #another range not overlapping with 10-20
    # print("---adding third interval")
    # myRM.addRange(21, 23) #another range not overlapping with 10-20
    # print("---adding an overlappign high bound interval")
    # myRM.addRange(15, 25) # range that overlaps with 10-20
    # print("---adding an overlapping low bound interval")
    # myRM.addRange(10, 20) # range that overlaps 10-20 lower bound
    # print("---adding encapsulating interval")
    # myRM.addRange(4, 26) # range that overlaps all current ranges
    print("myRM.queryRange(10, 14)",myRM.queryRange(6, 12))
    # print("myRM.queryRange(13, 15)",myRM.queryRange(13, 15))
    # print("myRM.queryRange(16, 17)",myRM.queryRange(16, 17))


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
