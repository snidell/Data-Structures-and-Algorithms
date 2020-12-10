
import math
class Solution:
    def num_palindrome(self,x:int)-> bool:
        if x <= 0:
            return x==0
        num_digits = math.floor(math.log10(x))+1
        # this is also possible
        #num_digits = len(str(x))
        msd_mask = 10**(num_digits-1)
        for i in range(num_digits//2):
            if x // msd_mask != x % 10:
                return False
            x %= msd_mask
            x //= 10
            msd_mask//=100
        return True

    # x =20002
    # num digits = 5
    # msd_mask 10**4 => 10000
    # range = (5//2) ==>2
    # -----loop1
    # x//msd_mask != x%10
    # 20002 // 10000 ==> 2     20002 %10 ==>2
    # x %= msd_mask   20002 %10000 ==>2
    # x//=10    2 //10 ==>0
    #msd_mask //=100  ==>10000//100 ==> 100
    #-------loop 2
    # 000 /100 ==> 000      000% 10  ==> 0
    # 0 % 100 ==> 0
    # x//10 ==> 0
    # 100//100 ==> 0
    # done




if __name__ =="__main__":
    mySolution = Solution()
    print(mySolution.num_palindrome(20002))
    print(mySolution.num_palindrome(0))
