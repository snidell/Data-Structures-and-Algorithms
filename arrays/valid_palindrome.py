# 680. Valid Palindrome I
# Given a string s, return true if the s can be palindrome after deleting at
# most one character from it.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        # loop through string from each end
        # compae char if good continue
        # if not comapare left with right/peakright
        # compare right with left/peak left
        # if they are the same our count is 1
        high = len(s) -1
        lo = 0
        count = 0

        while lo < high:
            print(lo,high)
            print(s[lo],s[high])
            if s[lo] == s[high]:
                lo += 1
                high -=1
                continue
            else:
                if s[lo] == s[high-1]:
                    high -= 1
                elif s[lo+1] == s[high]:
                    lo+=1
                count +=1
            if count > 1:
                break
        return True if count <=1 else False


if __name__ =="__main__":
    mySolution = Solution()
    myString = "abbra-cadabra"
    string = "cdbeeeabddddbaeedebdc"
    print(mySolution.validPalindrome(string))
