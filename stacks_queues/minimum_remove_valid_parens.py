# Leetcode 1249. Minimum Remove to Make Valid Parentheses

# Given a string s of '(' , ')' and lowercase English characters.
#
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any
# positions ) so that the resulting parentheses string is valid and return any
# valid string.
#
# Formally, a parentheses string is valid if and only if:
#
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.

class Solution:
    def minRemoveToMakeValid(self,s:str)->str:
        # keep track of what indices to remove when rebuilding string
        indexes_to_remove = set()
        # holds the count for each parent pair. Positive == too many lefts. Negative == too many rights
        stack = []
        for i, c in enumerate(s):
            # normal letter
            if c not in "()":
                continue
            if c =="(":
                stack.append(i)
            # if the stack is empty we need to track and we get a ")" we need to remove later
            elif not stack:
                indexes_to_remove.add(i)
            # if we have a matching ")" then its valid and we dont need ot track it
            else:
                stack.pop()
        # stack holds any residual parens left over. the set hold known sets that dont match
        indexes_to_remove = indexes_to_remove.union(set(stack))

        # now build the string
        string_builder = []
        for i,c in enumerate(s):
            if i not in indexes_to_remove:
                string_builder.append(c)
        return "".join(string_builder)



if __name__ =="__main__":
    mySolution = Solution()
    s = "lee(t(c)o)de)"
    print(mySolution.minRemoveToMakeValid(s))
