from typing import List
import collections
class Solution:
    def wordsTyping(self, sentence, rows, cols):
        mystr = ' '.join(sentence)
        # add space at the end
        mystr+=' '
        string_length = len(mystr)
        start = 0;
        for i in range(rows):
            # 0  +  8
            # 6  +  8
            # 12  +  8
            # 18  +  8
            # 24  +  8
            # 30  +  8
            start = start + cols;

            if (mystr[start % string_length] == ' '):
                start+= 1;
            else :
                while (start > 0 and mystr[(start-1) % string_length] != ' '):
                    start-=1;

        return start // string_length

    



if __name__ =="__main__":
    mySolution = Solution()
    words = ["hello","world"]
    nums = [1,2,3,4,5,6,7,8,9]
    print(sum(nums[0:3]))
    print(mySolution.wordsTyping(words,6,8))
