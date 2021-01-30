from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self._capacity = capacity


    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]


    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self._capacity:
            self.popitem(last = False)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ =="__main__":
    myLRU = LRUCache(4)
    myLRU.put("12",86)
    myLRU.put("13",12)
    myLRU.put("14",21)
    myLRU.put("15",34)
    myLRU.put("16",45)
    print(myLRU.get("12"))
    print(myLRU.get("32"))
    print(myLRU.get("34"))
    print(myLRU.get("13"))
