# Leetcode 809. Expressive Words
# Sometimes people repeat letters to represent extra feeling, such as
# "hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo",
# we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".
#
# For some given string S, a query word is stretchy if it can be made to be equal
# to S by any number of applications of the following extension operation: choose
#  a group consisting of characters c, and add some number of characters c to the
#  group so that the size of the group is 3 or more.
#
# For example, starting with "hello", we could do an extension on the group "o"
# to get "hellooo", but we cannot get "helloo" since the group "oo" has size
# less than 3.  Also, we could do another extension like "ll" -> "lllll" to
# get "helllllooo".  If S = "helllllooo", then the query word "hello" would be
# stretchy because of these two extension operations:
# query = "hello" -> "hellooo" -> "helllllooo" = S.

# Given a list of query words, return the number of words that are stretchy.
#
# Example:
# Input:
# S = "heeellooo"
# words = ["hello", "hi", "helo"]
# Output: 1
# Explanation:
# We can extend "e" and "o" in the word "hello" to get "heeellooo".
# We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.


import itertools
from typing import List

class Solution(object):
    # time complexity O(QK) where Q is the length of the words and k is max length of the word
    # Space complexity O(k)
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def RLE(S):
            letters = []
            lengths = []
            for letter, lg in itertools.groupby(S):
                letters.append(letter)
                lengths.append(len(list(lg)))
            return letters,lengths

        def valid_count(c1,c2):
            result = True
            for c1, c2 in zip(count, count2):
                # weird edge case if original string has a count of two and
                # current word has a count of 1 its still not valid
                # example helo is not strechy of heeellooo because the word only
                # has 1 L and the case strign only has 2 L's
                if c1==2 and c2==1:
                    return False
                # if current string has a letter longer than three or enough to accomodate the word letters
                # or if they are exact lengths
                if not(c1 >= max(c2, 3) or c1 == c2):
                    return False
            return result

        letters, count = RLE(S)
        print(letters,count)
        ans = 0
        for word in words:
            letters2, count2 = RLE(word)
            print(letters2,count2)
            if letters2 != letters: continue
            if valid_count(count,count2):
                ans += 1

        return ans


if __name__ =="__main__":
    mySolution = Solution()
    myString ="heeellooo"
    words = ["hello", "hi", "helo"]
    print(mySolution.expressiveWords(myString,words))
