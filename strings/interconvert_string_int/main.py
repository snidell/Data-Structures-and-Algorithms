import functools
import string
class Solution():
    def int_to_string(self,x: int) -> str:
        is_negative = False
        if x < 0:
            x,is_negative = -x, True
        s = []
        while True:
            # x%10 get last number
            # ord('0') reverse of chr() returns 48 which is ASCII int representation for zero
            # chr() convert 48+ x %10
            s.append(chr(ord('0')+x %10))
            x //=10
            if x ==0:
                break

        return ('-' if is_negative else '')+''.join(reversed(s))
    def string_to_int(self,s:str)->int:
        # reduce starts at the first two elements and slides applying the function to the next
        #running_sum, c: running_sum*10+string.digits.index(c) given 123
        # first iteration running_sum ==1 and c =2 ==> 1*10+2 ==>12 next iteration 12*10+3 ==>123
        # s[s[0] in '-+':] if the first index has a -+ put in the first index
        is_negative = 1
        if s[0] == "-":
            is_negative = -1
        running_sum = 0
        for i in range(1,len(s)):
            running_sum = running_sum * 10 + string.digits.index(s[i])
            print(running_sum)
        return is_negative * running_sum

        # return (-1 if s[0]== "-" else 1)*functools.reduce(
        #     lambda running_sum, c: running_sum*10+string.digits.index(c)
        #     ,s[s[0] in '-+':],0)


if __name__ =="__main__":
    mySolution = Solution()
    print(mySolution.int_to_string(-123))
    print(mySolution.string_to_int("-2222233"))
