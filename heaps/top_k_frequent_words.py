import collections
import heapq

class Solution:
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        print(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

if __name__ =="__main__":
    mySolution = Solution()
    words = ["i", "love", "leetcode", "i", "love", "coding","dumb","silly","i","love","cars"]
    k = 2
    print(mySolution.topKFrequent(words,k))
