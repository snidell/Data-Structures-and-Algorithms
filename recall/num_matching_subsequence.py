import collections
from typing import List

class WordIterator:
    def __init__(self,word):
        self.word = word
        self.current_key = 0
    def pop(self):
        # BB
        #
        if self.current_key != None and self.current_key <= len(self.word) -1:
            letter = self.word[self.current_key]
            self.current_key += 1
            return letter
        else:
            self.current_key = None
            return None



class Solution:
    # def num_matching_subseq(self,S:str,words:List[str])-> int:
    #     # loop through array and fill hashmap with letter key  and value of string iterator
    #     myMap = collections.defaultdict(list)
    #     for it in map(iter,words):
    #         myMap[next(it)].append(it)
    #
    #     for c in S:
    #         if c in myMap:
    #             for it in myMap.pop(c,()):
    #                 myMap[next(it,None)].append(it)
    #
    #
    #     return len(myMap[None])

    def num_matching_subseq(self,S:str,words:List[str])-> int:
        myMap = collections.defaultdict(list)
        for word in words:
            myMap[word[0]].append(WordIterator(word))

        for key in myMap:
            print("key:",key)
            for obj in myMap[key]:
                print(obj.word)

        for c in S:
            if c in myMap:
                for it in myMap[c]:
                    nextLetter = it.pop()
                    myMap[nextLetter].append(it)
            print("----------------")
            for key in myMap:
                print("key:",key)
                for obj in myMap[key]:
                    print(obj.word)

        for obj in myMap[None]:
            print(obj.word)
        return len(myMap[None])

if __name__ =="__main__":
    mySolution = Solution()
    s = "abcde"
    words = ["a","bb","acd","ace"]
    print(mySolution.num_matching_subseq(s,words))
