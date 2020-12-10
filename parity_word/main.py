
# COMPUTING THE PARITY OF A WORD
# The parity of a binary word is 1 if the number of ls in the word is odd;
# otherwise, it is 0. For example, the parity of 1011 is 1, and the parity of
# 10001000 is 0. Parity checks are used to detect single bit errors in data
# storage and communication. It is fairly straightforward to write code that
# computes the parity of a single 64-bit word.

# How would you compute the parity of a very large number of 64-bit words?


class Solution:
    # time cpmplexity 0(n) where n is the word size of the number. in this case 4
    def brute(self, x:int)->int:
        result = 0
        while x:
            # where x is int(10) and bin(1010)
            # x & 1 says get the last bits ^= takes the value of the last bit and XOR it
            # 0000 ^= 1010 & 0001
            # 0000 ^= 0 & 1 evauluate last bit
            # 0000 ^= 0
            # 0 ^= 0
            # result = 0
            # shift bits x >>1 1010 becomes 101
            #---next loop
            # 000^= 101 ^ 001
            # 000^= 1 & 1
            #0^=1
            # result = 1
            # shift bits x >>1 101 becomes 10
            #---next loop
            # 01 ^= 10 & 01
            # 01 ^= 0 & 1
            # 1 ^= 0
            #result = 1
            # shift bits x >> 1 10 becomes 1
            #-------next loop
            # 1 ^= 1 & 1
            # 0 ^= 1
            # result = 0

            result ^= x & 1
            print("new result:",result)
            # shifts the int value by 1 bit
            x >>= 1
        return result

    # time complexity is 0(k) where k is the number of 1s in a binary representation of the word
    def check_ones(self,x:int)->int:
        # commit x&(x-1) to memory. This will "erase" the lowest set bit
        # example: x= 00101100 (dec(44))
        # x-1 =43 or bin(00101011)
        # x&(x-1)  00101100 & 00101011 = 00101000
        result = 0
        while x:
            result ^=1
            x = x&(x-1)

        return result
    # time complexity O(log(n)) where n is the word size
    def bit_slide(self,x:int)->int:
        x ^= x >> 32
        x ^= x >> 16
        x ^= x >> 8
        x ^= x >> 4
        x ^= x >> 2
        x ^= x >> 1
        return x & 1
    #---VARIANT-- Write expression  that use bitwise operators, equality checks,
    #and Boolean operators to do the following in o(1) time
    # *right propagate the right most set bit in x ex. 01010000 -->01011111
    # *Compute x mod power of two ex. returns 13 for 77 mod 64
    # *Test if x is power of 2 1,2,4,8,....
    def propagate(self,x:int)->int:
        return x|x-1

    def bit_mod(self,x:int,y:int)->int:
        return x^y

    # binary powers of 2 have the left most bit set

    def power_two(self,x:int)->int:
        # 10 == False
        # 16 == True
        #(10) == 1010
        # x-1 == 1001
        # x & x-1   1010 & 1001 === 1000
        # not(1000) == 0111

        #(16) ==10000
        #x-1 == 01111
        # x & x-1  === 10000 & 01111 =00000
        # not(00000) == 1111True
        return not(x&(x-1))





if __name__ =="__main__":
    mySolution = Solution()
    print(mySolution.brute(10))
    print(mySolution.check_ones(10))
    print(mySolution.bit_slide(215))
    print(mySolution.propagate(80))
    print(mySolution.power_two(10))
    print(mySolution.power_two(16))
