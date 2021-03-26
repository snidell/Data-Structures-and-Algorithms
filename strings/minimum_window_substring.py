# Leetcode 727. Minimum Window Subsequence
# Given strings S and T, find the minimum (contiguous) substring W of S, so that
# T is a subsequence of W.
#
# If there is no such window in S that covers all characters in T, return the
# empty string "". If there are multiple such minimum-length windows, return the
# one with the left-most starting index.
#
# Example 1:
#
# Input:
# S = "abcdebdde", T = "bde"
# Output: "bcde"
# Explanation:
# "bcde" is the answer because it occurs before "bdde" which has the same length.
# "deb" is not a smaller window because the elements of T in the window must
# occur in order.

class Solution:
    def minWindow(self, S, T):
        # Find - Get ending point of subsequence starting after S[s]
        # returns the ending index of the next subsequence
        def find_subseq(s):
            t = 0
            while s < len(S):
                if S[s] == T[t]:
                    t += 1
                    if t == len(T):
                        break
                s += 1
            # Ensure last character of T was found before loop ended
            return s if t == len(T) else None

        # Improve - Get best starting point of subsequence ending at S[s]
        def improve_subseq(s):
            t = len(T) - 1
            while t >= 0:
                if S[s] == T[t]:
                    t -= 1
                s -= 1
            return s+1

        s, min_len, ans = 0, float('inf'), ''

        while s < len(S):
            # Find end-point of subsequence
            # for this example it first finds 4 abcdE
            # then 8 abcdebddE
            end = find_subseq(s)
            if not end:
                break

            # Improve start-point of subsequence by moving the left pointer
            # to do this we move from the right pointer backwards to the last letter in the sequence
            start = improve_subseq(end)
            print(start)

            # Track min length
            # if we have a smaller sequence then record it
            if end-start + 1 < min_len:
                min_len = end - start + 1
                ans = S[start:end + 1]

            # Start next subsequence search
            s = start + 1

        return ans




if __name__ =="__main__":
    mySolution = Solution()
    S = "abcdebdde"
    T = "bde"
    print(mySolution.minWindow(S,T))
