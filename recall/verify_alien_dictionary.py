
from typing import List
import itertools
class Solution:
    def is_Alien_Sorted(self,words:List[str],order:str)->bool:
        letter_map = {}
        # preload letter value in m,ap O(n)
        for idx,letter in enumerate(order):
            letter_map[letter] = idx

        result = True
        for idx in range(1,len(words)):
            word1 = words[idx-1]
            word2 = words[idx]
            for c1,c2 in itertools.zip_longest(word1,word2):
                if c1==c2:
                    continue
                # second word shorter than first
                if c2 == None:
                    result = False
                    break
                if c1 == None:
                    break
                # we are lexigraphically correct
                if letter_map[c1] < letter_map[c2]:
                    break
                # letters out of order
                if letter_map[c1] > letter_map[c2]:
                    break


        return result


if __name__ =="__main__":
    mySolution = Solution()
    words = ["hello","leetcode"]
    words2 = ["apple","app"]
    words3 = ["app","apple"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    print(mySolution.is_Alien_Sorted(words3,order))
