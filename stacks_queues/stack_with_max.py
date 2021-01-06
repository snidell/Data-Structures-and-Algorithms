# 8.1 IMPLEMENT A STACK WITH MAX APl
# Design a stack that includes a max operation, in addition to push and pop.
# The max method should return the maximum value stored in the stack.
import collections
from typing import List
class Stack:
    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax',
                                                    ('element', 'max'))
    def __init__(self)->None:
        self._element_with_cached_max: List[Stack.ElementWithCachedMax] = []

    def empty(self) -> bool:
        return len(self._element_with_cached_max) == 0
    def max(self):
        return self._element_with_cached_max[-1].max
    def pop(self)->int:
        if len(self._element_with_cached_max) > 0:
            return self._element_with_cached_max.pop().element
        else:
            return None
    def push(self,x:int)-> None:
        self._element_with_cached_max.append(self.ElementWithCachedMax(
            x, x if self.empty() else max(x,self.max())))
    def print(self):
        for i in range(len(self._element_with_cached_max)):
            print(self._element_with_cached_max[i])

if __name__ == "__main__":
    myStack = Stack()
    myStack.push(1)
    myStack.push(6)
    myStack.push(-5)
    myStack.push(100)
    myStack.push(3)
    myStack.print()
    print(myStack.max())
    print(myStack.pop())
    print(myStack.pop())
    print(myStack.empty())
    print(myStack.pop())
    print(myStack.pop())
    print(myStack.pop())
    print(myStack.pop())
    print(myStack.pop())
    print(myStack.pop())
    print(myStack.empty())
