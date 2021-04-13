import heapq

class LFUCache():

    def __init__(self, capacity):
        self.capacity = capacity
        self.time = 0
        self.map = {}               # key to value
        self.freq_time = {}         # key to (freq, time)
        self.priority_queue = []    # (freq, time, key), only updated when new key is added
        self.update = set()         # keys that have been get/put since last new key was added

    # O(1) Get
    def get(self, key):
        self.time += 1

        if key in self.map:
            freq, _ = self.freq_time[key]
            self.freq_time[key] = (freq + 1, self.time)
            self.update.add(key)
            return self.map[key]

        return -1

    # O(1) if key is in the map already else O(logk) when we add a new item to cache without exvicting
    # O(klogk) if an item needs to be evicted
    def put(self, key, value):
        if self.capacity <= 0:
            return

        self.time += 1
        # if key is not in the map
        if not key in self.map:
            # if we are at capacity we need to determine who is evicted via the min heap
            if len(self.map) >= self.capacity:      # must remove least frequent from cache

                while self.priority_queue and self.priority_queue[0][2] in self.update:
                    # whilst (least frequent, oldest) needs to be updated, update it and add back to heap
                    _, _, k = heapq.heappop(self.priority_queue)
                    f, t = self.freq_time[k]
                    heapq.heappush(self.priority_queue, (f, t, k))
                    self.update.remove(k)

                # remove (least frequent, oldest)
                _, _, k = heapq.heappop(self.priority_queue)
                self.map.pop(k)
                self.freq_time.pop(k)

            self.freq_time[key] = (0, self.time)
            heapq.heappush(self.priority_queue, (0, self.time, key))
        # If the key is already in the map update frequency
        else:
            freq, _ = self.freq_time[key]
            self.freq_time[key] = (freq + 1, self.time)
            self.update.add(key)

        print(self.priority_queue)

        self.map[key] = value



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    cache = LFUCache(5)
    # Input
    # ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
    # [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
    # Output
    # [null, null, null, 1, null, -1, 3, null, -1, 3, 4]

    cache.put(1,1)
    cache.put(2,2)
    # cache.get(1)
    # cache.put(3,3)
    # cache.get(2)
    # cache.get(3)
    # cache.put(4,4)
    # cache.put(5,5)
    # cache.put(6,6)
    # cache.put(7,7)
    # cache.put(8,8)
    # cache.get(1)
    # cache.get(3)
    # cache.get(4)
    # cache.get(1)
    # cache.get(8)
    # cache.get(1)
    # cache.get(6)
    # cache.get(1)
