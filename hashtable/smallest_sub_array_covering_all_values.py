# 12.6 FIND THE SMALLEST SUBARRAY COVERING ALL VALUES
# Write a program which takes an array of strings and a set of strings, and
# return the indices of the starting and ending index of a shortest subarray of
# the given array that "covers" the set, i.e., contains all strings in the set.

# Hint: What is the maximum number of minimal subarrays that can cover the query?
import collections
from typing import List
Subarray = collections.namedtuple('Subarray',('start','end'))
class Solution:
    def find_smallest_subarray_covering_set(self, paragraph:List[str],
                                            keywords: List[str])->Subarray:
        keywords_to_cover = collections.Counter(keywords)
        print(keywords_to_cover)
        result = Subarray(start=-1, end=-1)
        remaining_to_cover = len(keywords)
        left = 0

        for right, word in enumerate(paragraph):
            print(word)
            if word in keywords:
                keywords_to_cover[word] -= 1
                if keywords_to_cover[word] >= 0:
                    remaining_to_cover -=1

            # once we found both key words and quanitites   update the results
            # with the new index of cat...then banana. moveleft pointer until
            # we reach next keyword update result if the span is smaller
            print("words_remaing_to_cover",remaining_to_cover)
            while remaining_to_cover == 0:
                print("....",word," result ",result)
                # is this the first time we are updating the subarray ?
                # or is the span smaller(better) then the current. then update the span
                if result == Subarray(start=-1, end = -1) or right - left < result.end - result.start:
                    result = Subarray(start = left, end = right)
                p1 = paragraph[left]
                if p1 in keywords:
                    keywords_to_cover[p1] += 1
                    if keywords_to_cover[p1] > 0:
                        remaining_to_cover += 1
                left += 1
        return result

if __name__ =="__main__":
    mySolution = Solution()
    myWords = ["apple","banana","apple","apple","dog","cat","dog","banana","apple",
     "cat","dog"]
    mySearch = ["banana","cat"]
    print("given my words: ",myWords)
    print("find the smallest subbarray in which these words are found", mySearch)
    print(mySolution.find_smallest_subarray_covering_set(myWords,mySearch))
