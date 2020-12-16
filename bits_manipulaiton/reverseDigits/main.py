class Solution:
    # brute force convert to a string and call .reverse()
    # better way Generalizing, let the input be k. If k > 0, then k mod 10 is
    # the most significant digit of the result and the subsequent digits are
    # the reverse of k/10. Continuing with the example, we iteratively update
    # the result and the input as 2 and 113, then 23 and 11, then 231 and 1,
    #  then 2311.
    # For general le, we record its sign, solve the problem for |k|,
    #  and apply the sign to the result.
    # time complexity 0(n)
    def reverseDigits(self,x:int)->int:
        result, x_remaining = 0,abs(x)
        while x_remaining:
            result = result * 10 +x_remaining %10
            x_remaining //= 10

        return -result if x<0 else result

        # x =103
        #result = result*10+ x_remaining %10
        # 0*10 +103 %10 = 0 + 3 ==>3
        # x_remaining 103/10 ==>10
        # -------
        # 3*10 + 10% 10 ==>30 + 0 ==>30
        # x_remaining 10/10 ==> 1
        #------
        #30 *10 +1 %10 ==300 + 1 ===>301




if __name__=="__main__":
    mySolution = Solution()
    print(mySolution.reverseDigits(103))
