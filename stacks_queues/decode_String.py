# 394. Decode String

# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the
# square brackets is being repeated exactly k times. Note that k is guaranteed to
# be a positive integer.
#
# You may assume that the input string is always valid; No extra white spaces,
# square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any digits
# and that digits are only for those repeat numbers, k. For example, there won't
# be input like 3a or 2[4].



Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n = len(s)
        result =""

        for i in range(n):
            if s[i] != ']':
                stack.append(s[i])
            else:
                print(stack)
                decode_string = ""
                while True:
                    letter = stack.pop()
                    if letter == '[':
                        break
                    #word will be backward here
                    decode_string +=letter
                # loop while number
                num = int(stack.pop())
                print("decode string:",decode_string)
                decode_string = num * decode_string
                # push decoded word back onto stack word becomes forward again
                for i in range(len(decode_string)-1,-1,-1):
                    print(decode_string[i])
                    stack.append(decode_string[i])
        for i in range(len(stack)):
            result+=stack[i]
        return result

if __name__ =="__main__":
    mySolution = Solution()
    myString = "3[a]2[bc]"
    # myString = "3[a2[c]]"
    myString = "100[leetcode]"
    # 3[acc] accaccacc
    print(mySolution.decodeString(myString))
