import string

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        myMap = {}
        for idx,letter in enumerate(string.ascii_lowercase):
            #store letter and x,y coordinate. The matrix is 5 slots wide
            y = idx // 5
            x = idx % 5
            myMap[letter] = [x,y]

        # now we need to move from the start position (0,0) to the next letters
        currentx = currenty = 0
        result = []
        for letter in target:
            xtarget,ytarget = myMap[letter]

            print(currentx,currenty,"target",xtarget,ytarget)
            # go left
            if xtarget < currentx:result.append('L'* (currentx-xtarget))
            # go up
            if ytarget < currenty: result.append('U'*(currenty-ytarget))
            # go down
            if ytarget >currenty: result.append('D'*(ytarget-currenty))

            # go right
            if xtarget > currentx: result.append('R'*(xtarget-currentx))
            result+="!"
            currentx,currenty = xtarget,ytarget
        return "".join(result)

if __name__ =="__main__":
    mySolution = Solution()
    print(mySolution.alphabetBoardPath("leet"))
