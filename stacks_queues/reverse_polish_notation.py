# 8.2 EVALUATE RPN EXPRESSIONS
# Write a program that takes an arithmetical expression in RPN and returns
# the number that the expression evaluates to.
from typing import List
class ReversePolishNotation:
    def evaulate(self,expression:str)-> int:
        intermeadiate_results: List[int] = []
        delimiter = ","
        operators = {
            '+': lambda y,x:x+y,
            '-': lambda y,x: y-x,
            '*': lambda y,x: y*x,
            '/': lambda y,x: y//x
        }
        for token in expression.split(delimiter):
            if token in operators:
                intermeadiate_results.append(
                    operators[token](
                        intermeadiate_results.pop(),intermeadiate_results.pop()))
            else: # token is a number.
                intermeadiate_results.append(int(token))
        return intermeadiate_results[-1]

if __name__ == "__main__":
        mySolution = ReversePolishNotation()
        print(mySolution.evaulate("3,4,+,2,*,1,+")) #15
        print(mySolution.evaulate("3,4,2,1,+,*,*")) #36
