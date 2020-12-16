import string
# 6.2 BASE CONVERSION
class Solution:
    def convert_to_base(self,num_as_string:str,b1:int,b2:int)->str:
        result =[]
        as_int = 0
        for i in range(len(num_as_string)):
            as_int += string.hexdigits.index(num_as_string[i].lower())*b1**(len(num_as_string)-1-i)
        result= ""
        while as_int:
            result+=(string.hexdigits[as_int%b2])
            as_int//=b2


        return ''.join(reversed(result))






if __name__ =="__main__":
    mySolution = Solution()
    # convet (615)base7 to base 13 ==1A7
    print(mySolution.convert_to_base("615",7,13))
