# 844. Backspace String Compare
# Given two strings S and T, return if they are equal when both are typed into
# empty text editors. # means a backspace character.
#
# Note that after backspacing an empty text, the text will continue empty.
#
# Example 1:
#
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:
#
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s1Stack = []
        s2Stack = []
        for char in S:
            if char.isalpha():
                s1Stack.append(char)
            if char == "#" and s1Stack:
                pre_string = s1Stack.pop()
        for char in T:
            if char.isalpha():
                s2Stack.append(char)
            if char == "#" and s2Stack:
                pre_string = s2Stack.pop()

        # we can compare stacks here now instead of making it a string
        print(s1Stack,s2Stack)
        return s1Stack == s2Stack


if __name__ =="__main__":
    mySolution = Solution()
    s1 = "ab##"
    s2 = "c#d#"
    print(mySolution.backspaceCompare(s1,s2))
