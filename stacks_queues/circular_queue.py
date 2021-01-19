class CircularQueue:
    SCALE_FACTOR = 2
    def __init__(self,capacity:int) -> None:
        self._entries = [0]*capacity
        self._head = self._tail = self._num_queue_elements = 0

    def enqueue(self,x: int) -> None:        
        # do we need to make the array bigger?
        if self._num_queue_elements == len(self._entries):
            self._entries = (self._entries[self._head:] +
                             self._entries[:self._head])
            # reset head and tail

            self._head, self._tail = 0, self._num_queue_elements
            self._entries +=[0] * (len(self._entries) *
                        CircularQueue.SCALE_FACTOR - len(self._entries))
            print("after adding new entries")
            print(self._entries)

        self._entries[self._tail] = x
        self._tail = (self._tail + 1) % len(self._entries)
        self._num_queue_elements += 1

    def dequeue(self) -> int:
        self._num_queue_elements -=1
        result = self._entries[self._head]
        self._head = (self._head + 1) % len(self._entries)
        return result

    def size(self) -> int:
        return self._num_queue_elements


if __name__ =="__main__":
    myQueue = CircularQueue(3)
    myQueue.enqueue(20)
    myQueue.enqueue(2)
    myQueue.enqueue(3)
    myQueue.enqueue(-3)
    myQueue.enqueue(5)
    myQueue.enqueue(3)
    myQueue.enqueue(-5)
    print(myQueue.size())
    myQueue.dequeue()
    myQueue.dequeue()
    myQueue.dequeue()
    myQueue.enqueue(-5)
