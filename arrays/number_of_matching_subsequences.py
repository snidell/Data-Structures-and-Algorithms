# Given string S and a dictionary of words words, find the number of words[i]
# that is a subsequence of S.
#
# Example :
# Input:
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three words in words that are a subsequence of
# S: "a", "acd", "ace".
#
# https://leetcode.com/problems/number-of-matching-subsequences/discuss/117634/Efficient-and-simple-go-through-words-in-parallel-with-explanation/
import collections

class Solution:
    def numMatchingSubseq(self, S, words):
        # words waiting for the next letter
        # key: letter values: a list of iterator based strings that contain the words
        # example: {a: "acd"}
        waiting = collections.defaultdict(list)
        for it in map(iter, words):
            waiting[next(it)].append(it)
        # as the letter is matched the word is moved to the next "waiting slot"
        # example the word "acd" would start at {a:["(a)cd"]}
        # once a is scaned it is removed from a and moved to c and the iterator is updated
        # now the waiting dictionary look like this {c:{a(c)d}}
        # once the iterator is exhausted it is moved to the waiting[None]
        # position this will contain all words that can be spelled
        for c in S:
            # pop each item off the list in that letter group
            # if that eltter doesnt exist return a empty list and the for loop will not execute
            # if you reference a key in a dictionary that doesnt exist a KeyError will be thrown
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)

        return len(waiting[None])

if __name__ =="__main__":
    mySolution = Solution()
    myString = "azbcde"
    words =["a", "bb", "acd", "ace"]
    print(mySolution.numMatchingSubseq(myString,words))
    myDict = {'a':["a","acd","ace"],'b':["bb"]}
    for c in myString:
        for it in myDict.pop(c,()):
            print("c:",c," it",it)
