# 16.2 COMPUTE THE LEVENSHTEIN DISTANCE
# Leetcode 72 Edit Distance

# The distance between two words as the minimum number of "edits" it would take
# to transform the misspelled word into a correct word, where a single edit is
# the insertion, deletion, or substitution of a single character. For example,
# the Levenshtein distance between "Saturday" and "Sundays" is 4-delete the first
# 'a' and 't', substitute 'r' by 'n' and insert the trailing 's'.
#
# Write a program that takes two strings and computes the minimum number of edits
# needed to transform the first string into the second string.

# Hint: Consider the same problem for prefixes of the two strings.

class Solution:
    # Time complexity : O(mn) as it follows quite straightforward for the inserted loops.
    # Space complexity : O(mn) since at each step we keep the results of all previous computations.
    def minDistance(self,word1: str,word2:str)-> int:
        n = len(word1)
        m = len(word2)

        if n*m ==0:
            return n+m
        # initialize the 2D array
        d = [[0] * (m +1) for _ in range(n + 1)]

        for i in range(n + 1):
            d[i][0] = i
        for j in range(m + 1):
            d[0][j] = j

        # DP compute

        for i in range(1, n + 1):
            for j in range(1,m + 1):
                left = d[i-1][j] + 1
                down = d[i][j -1] + 1
                left_down = d[i-1][j-1]
                if word1[i-1] != word2[j-1]:
                    left_down += 1
                d[i][j] = min(left,down,left_down)
        return d[n][m]





if __name__ =="__main__":
    mySolution = Solution()
    print(mySolution.minDistance("horse","ros"))


    #    #  R  O  S
    # # [0, 1, 2, 3]
    # H [1, 1, 2, 3]
    # O [2, 2, 1, 2]
    # R [3, 2, 2, 2]
    # S [4, 3, 3, 2]
    # E [5, 4, 4, 3]
