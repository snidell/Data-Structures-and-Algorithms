# 15.7 GENERATE STRINGS OF MATCHED PARENS
# Write a program that takes as input a number and returns all the strings with
# that number of matched pairs of parens.
#
# Hint: Think about what the prefix of a string of matched parens must look like.

# Leetcode 22 Generate Parentheses

from typing import List

class Solution:
    # time complexity The number C(k) of strings with le pairs of matched
    # parens grows very rapidly with le. Specifically, it can be shown that
    # C(k + 1) = summatiom from i=0 to k (k over i)/(k+1), which solves to
    # (2k)!/((k!(k + 1)!).
    def generate_parenthesis(self,n:int)-> List[str]:
        def gen_paren_helper(left_needed,right_needed,valid_prefix,result=[]):
            if left_needed > 0: #able to insert '('
                gen_paren_helper(left_needed - 1,right_needed,valid_prefix +'(')
            if left_needed < right_needed:
                # able to inset ')'
                gen_paren_helper(left_needed,right_needed - 1,valid_prefix + ')')
            # exhausted this set so add it to the result
            print(valid_prefix)
            if not right_needed:
                result.append(valid_prefix)
            return result

        return gen_paren_helper(n,n,valid_prefix ='')

if __name__ =="__main__":
    mySolution = Solution()
    print(mySolution.generate_parenthesis(3))
    # valid_prefix builds left uses stack pop to add the right
    # ((()))
    # ((())
    # ((()
    # (((
    # (()())
    # (()()
    # (()(
    # (())()
    # (())(
    # (())
    # (()
    # ((
    # ()(())
    # ()(()
    # ()((
    # ()()()
    # ()()(
    # ()()
    # ()(
    # ()
    # (
    # result:
    # ['((()))', '(()())', '(())()', '()(())', '()()()']
