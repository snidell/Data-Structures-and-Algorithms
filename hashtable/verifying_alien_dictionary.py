# 953. Verifying an Alien Dictionary
# https://leetcode.com/problems/verifying-an-alien-dictionary/
# in an alien language, surprisingly they also use english lowercase letters,
# but possibly in a different order. The order of the alphabet is some
# permutation of lowercase letters.
#
# Given a sequence of words written in the alien language, and the order of the
# alphabet, return true if and only if the given words are sorted lexicographicaly
# in this alien language.

from typing import List
import itertools
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        myMap = {}
        # loop through order O(N) load hashmap
        for idx,letter in enumerate(order):
            myMap[letter] = idx
        n = len(words)
        result = True

        for i in range(1,n):
            for l1,l2 in itertools.zip_longest(words[i-1],words[i]):
                # the second wor is shorter than the first this can't happen [apple,app]
                if l2 == None:
                    result = False
                    break
                # the first words is shorter than the secodn. this can happen [app,apple]
                if l1 == None:
                    break
                # letters are different but in order
                if myMap[l1]< myMap[l2]:
                    break
                # letters are different but out of order
                elif myMap[l1] > myMap[l2]:
                    result = False
                    break
                # otherwise their equal and we continue
        return result


if __name__ =="__main__":
    mySolution = Solution()
    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    # words = ["word","world","row"]
    # order = "worldabcefghijkmnpqstuvxyz"

    # words = ["apple","app"]
    # order = "abcdefghijklmnopqrstuvwxyz"
    print(mySolution.isAlienSorted(words,order))

# Example 1:
#
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
