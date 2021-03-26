# 295. Find Median from Data Stream
# The median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value and the median is the mean of the two
# middle values.
#
# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:
#
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data
# structure.
# double findMedian() returns the median of all elements so far. Answers within
# 10-5 of the actual answer will be accepted.

import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.median = 0
        self.min_heap = [] #holds the bigger numbers
        self.max_heap = [] #holds the smaller numbers



    def addNum(self, num: int) -> None:
        # first push to min heap and then pop resulting to max heap. this heapifies both the min and max heap
        heapq.heappush(self.max_heap,-heapq.heappushpop(self.min_heap,num))

        # two siezes for the heaps. either they are equal i size or min heap has one more
        if len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.min_heap,-heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        print("min:",self.min_heap)
        print("max:",self.max_heap)
        if len(self.min_heap) == len(self.max_heap) and len(self.min_heap) != 0:
            return 0.5 * (-self.max_heap[0] + self.min_heap[0])
        else:
            return self.min_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

if __name__ =="__main__":
    myMedian = MedianFinder()
    myMedian.addNum(3)
    print(myMedian.findMedian())
    myMedian.addNum(-1)
    print(myMedian.findMedian())
    myMedian.addNum(2)
    print(myMedian.findMedian())
    myMedian.addNum(6)
    print(myMedian.findMedian())
    myMedian.addNum(4)
    print(myMedian.findMedian())
    myMedian.addNum(5)
    print(myMedian.findMedian())
    myMedian.addNum(8)
    print(myMedian.findMedian())
