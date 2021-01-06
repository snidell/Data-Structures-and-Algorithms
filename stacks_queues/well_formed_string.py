# 8.3 ls A STRING WELL-FORMED?
# Write a program that tests if a string made up of the
# characters'(',')','[',']',"{' and"}' is well-formed.

class Solution:
    def is_well_formed(self,s:str)-> bool:
        left_chars, lookup = [], {'(': ')', '{': '}', '[': ']'}
        for c in s:
            if c in lookup:
                # if its a valid charcter add to stack
                left_chars.append(c)
            elif not left_chars or lookup[left_chars.pop()] != c:
                # if we have no more remaining charcters or the top charcter
                # does not match the current its corresponding bracket return false
                return False
        return not left_chars

if __name__ == "__main__" :
    mySolution = Solution()
    print(mySolution.is_well_formed("((()))")) #true
    print(mySolution.is_well_formed("({[]})")) #true
    print(mySolution.is_well_formed("({[})")) #frue
