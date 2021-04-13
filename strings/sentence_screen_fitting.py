from typing import List
import collections
class Solution:
    def wordsTyping(self, sentence, rows, cols):
        mystr = ' '.join(sentence)
        # add space at the end
        mystr+=' '
        string_length = len(mystr)
        start = 0;
        print("strign length:",string_length)
        for i in range(rows):
            # 0  +  8
            # 6  +  8
            # 12  +  8
            # 18  +  8
            # 24  +  8
            # 30  +  8
            start = start + cols;
            print("start:",start)
            # adjust the start point to a space as we cannot start the next word next to the previous
            if (mystr[start % string_length] == ' '):
                start+= 1
            else :
                # move the next start to the end of the string
                while (start > 0 and mystr[(start-1) % string_length] != ' '):
                    start-=1

            print("adjusted start",start)
        return start // string_length


if __name__ =="__main__":
    mySolution = Solution()
    words = ["hello","world"]
    print(mySolution.wordsTyping(words,2,300))
