class Solution:
    # time complexity for both are O(n) time and O(1) space
    def is_palindrome(self,x:str)->bool:
        for i in range(len(x)//2):
            if x[i] != x[~i]:
                return False
        return True

    def ans_palindrome(self,s:str)->bool:
        return all(s[i] == s[~i] for i in range(len(s) // 2))

if __name__ == "__main__":
    mySolution = Solution()
    s1 = "hello "
    s2 = "World"
    print(mySolution.is_palindrome("racecar"))
    print(mySolution.ans_palindrome("raczcar"))
    print(mySolution.ans_palindrome("HiHoSilver"))
    # other helpful string methods
    print(s1+s2)
    # is h in t ?
    print("h" in s1)
    # removes l from hello runs O(n)
    print(s1.strip("l"))
    # determines if the prefix passed starts in the string s1
    print(s1.startswith("hel"))
    print(s1.startswith("hey"))
    # determines if the suffix passed ends in the string s2
    print(s2.endswith("ld"))
    print(s2.endswith("no"))
    # splits on comma
    myList = 'Euclid,Axiom 5,Parallel Lines' .split(',')
    # ['Euclid', 'Axiom 5', 'Parallel Lines']
    print(myList)
    
