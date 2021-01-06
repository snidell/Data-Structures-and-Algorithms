import collections
# queues are FIFO approach. Queus are idel when order needs to be preserved
class Queue:
    def __init__(self)-> None:
        self._data: Deque[int] = collections.deque()
    def enqueue(self, x:int)-> None:
        self._data.append(x)

    def deque(self)-> int:
        self._data.popleft()
    def max(self)-> int:
        return max(self._data)
    def print(self)-> None:
        for i in self._data:
            print(i)


if __name__ == "__main__":
    myQueue = Queue()

    myQueue.enqueue(1)
    myQueue.enqueue(6)
    myQueue.enqueue(5)
    myQueue.enqueue(8)
    myQueue.enqueue(10)
    myQueue.enqueue(-3)
    myQueue.print()
    myQueue.deque()
    myQueue.print()
