class Solution:
    # compute the parity of the word is 1 if the number of 1s is odd otherise zero
    def parity(self,x:int)->int:
        result =0
        while x:

            result ^= x & 1
            x >>=1

        return result
    # nope
    def parity_better(self,x:int)->int:
        result =0

        while x:
            result ^=x & 1
            x &= x-1
        return result
    # no
    def parity_bit_slide(self,x:int)->int:
        x^= x>>32
        x^= x>>16
        x^= x>>8
        x^= x>>4
        x^= x>>2
        x^=x>>1
        return x & 1
    # propagate the right most bit set in x ex. 0101000 --> 01011111
    # no
    def propagate(self,x:int)->int:
        return x |x-1
    # yes
    def mod_power(self,x:int,y:int)->int:
        return x ^ y
    # no
    def if_power_of_2(self,x:int)->int:
        return not(x&(x-1))




if __name__ =="__main__":
    mySolution = Solution()
    print(mySolution.parity(11))
    print(mySolution.parity_better(10))
    print(mySolution.parity_bit_slide(187))
    print(bin(mySolution.propagate(40)))
    print(mySolution.mod_power(77,64))
    print(mySolution.if_power_of_2(15))
