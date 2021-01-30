# 12.1 TEST FOR PALINDROMIC PERMUTATIONS
# Write a program to test whether the letters forming a string can be permuted
# to form a palindrome. For example, "edified" can be permuted to form "deified"
# Hint: Find a simple characterization of strings that can be permuted to form a
# palindrome.

import collections
class Solution:
    def can_form_palindrome(s: str) -> bool:
        sum = 0
        print(collections.Counter(s))
        for v in collections.Counter(s).values():
            print(v)
            sum += v % 2
        print("sum: ",sum)
        return sum <=1


if __name__ == "__main__":
    mySolution = Solution
    print(mySolution.can_form_palindrome("abaa"))
