# 6.5 TEST PALINDROMICITI'
# For the purpose of this problem, define a palindromic string to be a string which when all the
# nonal.phanumeric are removed it reads the san1e front to back ignoring case. For example, "A man,
# a plan, a canal, Panama." and"Able was I, ere I saw Elba!" are palindromic, but "Ray a Ray" is not.
# Implement a function which takes as input a string s and returns tme ifs is a palindromic string.


# Time Complexity We spend O(1) per character, so the time complexity is O(n),
# where n is the length of s.
class Solution:
    def is_palindrome(self,s: str) -> bool:
        i,j=0,len(s)-1
        while i<j:
            # if i or j is not a letter increment/decrement
            while not s[i].isalnum():
                i += 1
            while not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                # if i or j is lowercase letter and != break
                return False
            # increment i and increment j to proceed on to the next letter
            i,j = i + 1, j - 1
        return True





if __name__ == "__main__":
    mySolution = Solution()
    print(mySolution.is_palindrome("A man,a plan, a canal, Panama.")) # True
    print(mySolution.is_palindrome("Fizz Buzz")) # False
