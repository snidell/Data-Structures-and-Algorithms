class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.length = 0
        self.max = size
        self.sum = 0
        self.queue = deque()

    def next(self, val: int) -> float:
        if self.length < self.max:
            self.length +=1
            self.queue.append(val)
            self.sum += val
        else:
            self.sum -= self.queue.popleft()
            self.queue.append(val)
            self.sum += val
        return self.sum/self.length





if __name__ =="__main__":
    mva = MovingAverage(3)


    print(mva.next(1))
    print(mva.next(10))
    print(mva.next(3))
    print(mva.next(5))


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
