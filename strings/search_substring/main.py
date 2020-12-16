# 6.12 FIND THE FIRST OCCURRENCE OF A SUBSTRING

# Given two strings s (the "search string") and t (the "text"), find the first
#  occurrence of s in t. returns the index of first char in the search word if found

# For a good hash function, the time complexity is O(m + n), independent
# of the inputs s and t, where m is the length of s and n is the length of t.
import functools
class Solution:
    def rabin_karp(self,t: str, s: str) ->int:
        if len(s) > len(t):
            return -1

        base = 26
        t_hash = functools.reduce(lambda h,c: h * base + ord(c), t[:len(s)], 0)
        s_hash = functools.reduce(lambda h,c: h * base + ord(c), s, 0)
        power_s = base ** max(len(s)-1, 0)
        print("power: ",power_s, "t_hash: ",t_hash," s_hash: ",s_hash)
        print(len(t))
        for i in range(len(s),len(t)):
            print("i:",i)
            if t_hash == s_hash and t[i-len(s):i]  == s:
                return i - len(s) # match found
            # update hash for incoming and outgoing letters
            # remove value of first letter from hash
            t_hash -= ord(t[i - len(s)]) * power_s
            # add value of new letter to hash
            t_hash = t_hash * base + ord(t[i])

        if t_hash == s_hash and t[-len(s):]  == s:
            return len(t) - len(s)
        return -1
if __name__ == "__main__":
    mySolution = Solution()
    print(mySolution.rabin_karp("Where in the world is carmen san diego","san"))
