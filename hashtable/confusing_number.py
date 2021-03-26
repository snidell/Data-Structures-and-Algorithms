# Given a number N, return true if and only if it is a confusing number, which
# satisfies the following condition:
#
# We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are
# rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5
# and 7 are rotated 180 degrees, they become invalid. A confusing number is a
# number that when rotated 180 degrees becomes a different number with each digit
# valid.



class Solution:
    def confusingNumber(self, N: int) -> bool:
        valid = [0, 1, 6, 8, 9]
        rotate = {0:0,1:1,6:9,8:8,9:6}
        tempN = N
        result = 0
        while tempN:
            current_number = tempN % 10
            # if its not a valid number then return False
            if not(current_number in valid):
                return False
            result= result *10 +rotate[current_number]
            tempN//=10

        if result!= N:
            return True
        else:
            return False


if __name__ =="__main__":
    mySolution = Solution()
    print(mySolution.confusingNumber(112))
    print(mySolution.confusingNumber(11))
    print(mySolution.confusingNumber(89))
    print(mySolution.confusingNumber(6))
