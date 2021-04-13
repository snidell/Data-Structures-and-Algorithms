# Leetcode 471. Encode String with Shortest Length
# Given a non-empty string, encode the string such that its encoded length is the
# shortest.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the
# square brackets is being repeated exactly k times.
#
# Note:
#
# k will be a positive integer.
# If an encoding process does not make the string shorter, then do not encode it.
# If there are several solutions, return any of them.
#
#
# Example 1:
#
# Input: s = "aaa"
# Output: "aaa"
# Explanation: There is no way to encode it such that it is shorter than the input
# string, so we do not encode it.
# Example 2:
#
# Input: s = "aaaaa"
# Output: "5[a]"
# Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
# Example 3:
#
# Input: s = "aaaaaaaaaa"
# Output: "10[a]"
# Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have
# the same length = 5, which is the same as "10[a]".
# Example 4:
#
# Input: s = "aabcaabcd"
# Output: "2[aabc]d"
# Explanation: "aabc" occurs twice, so one answer can be "2[aabc]d".
# Example 5:
#
# Input: s = "abbbabbbcabbbabbbc"
# Output: "2[2[abbb]c]"
# Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to
# "2[abbb]c", so one answer can be "2[2[abbb]c]".

class Solution:
    def encode(self, s):
        """
        :type s: str
        :rtype: str
        """
        N = len(s)
        dp = [[''] * N for _ in range(N)]

        for j in range(N):
            for i in range(j, -1, -1):
                sub = s[i:j+1]
                # print(sub, "j,i: ",j,i)
                dp[i][j] = sub
                if j - i >= 4:
                    for k in range(i, j):
                        # does the subsequence yield a bigger valid sequence if we choose that sequence
                        if len(dp[i][k] + dp[k+1][j]) < len(dp[i][j]):
                            dp[i][j] = dp[i][k] + dp[k+1][j]

                    subsub = sub + sub
                    print("subsub:",subsub)
                    # how many times does this sequence repeat
                    idx_repeat = subsub.find(sub, 1)
                    # form the candidate sequence in the form of N[sequence]
                    cand = str((j+1-i)//(idx_repeat)) + '[' + dp[i][i+idx_repeat-1] + ']'
                    # if this sequence is better than our previously stored sequence update the DP matrix
                    if len(cand) < len(dp[i][j]):
                        dp[i][j] = cand
        print(dp)
        return dp[0][N-1]


if __name__ =="__main__":
    mySolution = Solution()
    myString ="aabcaabcd"
    print(mySolution.encode(myString))
