class Solution:
    # write a program that takes double x and int y to compute x^y ignore overflow/underflow
    # if the elast significant bit is 0 then we can write this as  (x^(y/2))^2
    # else the bit is 1 and can be represented like x(x^(y/2))^2
    # if the number is negative y becomes negative and x become 1/x
    def pow(self,x:float,y:int)->float:
        result,power =1.0,y
        count = 0
        if y<0:
            power, x = -power, 1.0/x
        while power:
            count += 1
            # if the last bit is 1
            if power & 1:
                result *= x
            #x*x , power >> 1
            #2*2 =>4 , 100>> 1 => 10
            #4*4 =>16, 10 >>1 =>1
            #odd last bit
            #result *= x
            #1.0*16.0 =>16
            #return result of 16
            x,power = x*x, power >> 1
        print(count)
        return result


if __name__ == "__main__":
    mySolution = Solution()
    print(mySolution.pow(2,4))
