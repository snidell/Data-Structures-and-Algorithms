from typing import List


class Solution:
    def fit_sentence(self,sentence: List[str], rows:int, cols:int)-> int:
        myString = ' '.join(sentence)
        myString += ' '
        string_length = len(myString)
        start = 0
        for _ in range(rows):
            start = start + cols
            print(start)
            # if my string lands on a space
            if (myString[start % string_length] == ' '):
                start += 1
            else:
                while (start > 0 and myString[(start-1) % string_length] != ' '):
                    start-=1
            print("adjusted start: ",start)
        return start //string_length




if __name__ =="__main__":
    mySolution = Solution()
    sentence = ["a", "bcde", "fgh"]
    #   a-bcd-
    #   e-a---
    #   bcd-e-
    print(mySolution.fit_sentence(sentence,3,16))
