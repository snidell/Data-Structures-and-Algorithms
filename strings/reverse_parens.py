import re
class Solution:
    def reverseInParentheses(self,inputString):
        parens = []

        for i in range(len(inputString)):
            if inputString[i] == '(':
                parens.append(i)
            elif inputString[i] == ')':
                t = inputString[parens[-1]:i +1]
                inputString = inputString[:parens[-1]] + t[::-1] + inputString[i+1:]

                del parens[-1]
        result = ""
        for i in range(len(inputString)):
            if inputString[i] !=')' and inputString[i] != '(':
                result += inputString[i]
        return result




if __name__ =="__main__":
    mySolution = Solution()
    print(mySolution.reverseInParentheses("foo(bar)baz(blim)"))
