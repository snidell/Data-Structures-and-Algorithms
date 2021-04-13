# 15. 11 COmpute Grey Code
# Write a program which takes n as input and returns an n-bit Gray code.
# Hint: Write out Gray codes for n = 2, 3, 4.

from typing import List
class Solution:
    # tiem complexity Assuming we operate on integers that fit within the size
    # of the integer word, the time complexity T(n) satisfies T(n) = T(n - 1) +
    # 0(2^n-1). The time complexity is 0(2^n).
    def grayCode(self, n: int) -> List[int]:
        # print("n: ",n)
        if n == 0:
            return[0]
        # These implicitly begin with   0 at bit-index (n-1)
        gray_code_num_bits_minus_1 = self.grayCode(n-1)
        # Now add one to the bit index
        leading_bit_one = 1 << (n -1)
        # Process in reverse order to acheive reflection
        # of gray code
        # print(gray_code_num_bits_minus_1," ",leading_bit_one)
        return gray_code_num_bits_minus_1 + [leading_bit_one |
                i for i in reversed(gray_code_num_bits_minus_1)]


if __name__ =="__main__":
    mySolution = Solution()
    print(mySolution.grayCode(6))
