# You are given a license key represented as a string S which consists only
# alphanumeric character and dashes. The string is separated into N+1 groups
# by N dashes.
#
# Given a number K, we would want to reformat the strings such that each group
# contains exactly K characters, except for the first group which could be
# shorter than K, but still must contain at least one character. Furthermore,
# there must be a dash inserted between two groups and all lowercase letters
# should be converted to uppercase.
#
# Given a non-empty string S and a number K, format the string according to
# the rules described above.
#
# https://leetcode.com/problems/license-key-formatting/

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        # replace and uppercase string
        S = S.upper().replace('-', '')
        size = len(S)
        # find edge case
        if size % K == 0:
            s1 = K
        else:
            s1 = size % K
        ret = S[:s1]
        while s1 < size:
            ret = ret + '-' + S[s1:s1+K]
            s1 = s1 + K
        return ret



if __name__ == "__main__":
    soultion = Solution()
    # myString = "5F3Z-2e-9-w"
    myString = "2-5g-3-J"
    # myK = 4
    myK = 2
    print(soultion.licenseKeyFormatting(S=myString,K=myK))
