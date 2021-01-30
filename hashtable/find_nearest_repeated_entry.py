# 12.5 FIND THE NEAREST REPEATED ENTRIES IN AN ARRAY

from typing import List
class Solution:
    # time complexity is O(n) and space compelxity is O(d) where d is the distinct
    # entries in the array
    def find_nearest_rep(self,paragraph: List[str]) -> int:
        word_to_latest_index: Dict[str,int] = {}
        nearest_repeated_distance = float('inf')
        for i, word in enumerate(paragraph):
            if word in word_to_latest_index:
                latest_equal_word = word_to_latest_index[word]
                nearest_repeated_distance = min(nearest_repeated_distance,
                                            i - latest_equal_word)
            word_to_latest_index[word] = i

        if nearest_repeated_distance != float('inf'):
            return nearest_repeated_distance
        else:
            return -1


if __name__ == "__main__":
    mySolution = Solution()
    print(mySolution.find_nearest_rep(["All", "work", "and", "no", "play",
        "makes", "for", "no", "work", "no", "fun", "and", "no", "results "]))
    # result in 2 for no at 7 and 9
