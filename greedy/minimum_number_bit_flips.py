# 995. Minimum Number of K Consecutive Bit Flips (Hard)

# In an array A containing only 0s and 1s, a K-bit flip consists of choosing a
# (contiguous) subarray of length K and simultaneously changing every 0 in the
# subarray to 1, and every 1 in the subarray to 0.
#
# Return the minimum number of K-bit flips required so that there is no 0 in the
# array.  If it is not possible, return -1.
#
# Example 1:
#
# Input: A = [0,1,0], K = 1
# Output: 2
# Explanation: Flip A[0], then flip A[2].
# Example 2:
#
# Input: A = [1,1,0], K = 2
# Output: -1
# Explanation: No matter how we flip subarrays of size 2, we can't make the array
# become [1,1,1].
# Example 3:
#
# Input: A = [0,0,0,1,0,1,1,0], K = 3
# Output: 3
# Explanation:
# Flip A[0],A[1],A[2]: A becomes [1,1,1,1,0,1,1,0]
# Flip A[4],A[5],A[6]: A becomes [1,1,1,1,1,0,0,0]
# Flip A[5],A[6],A[7]: A becomes [1,1,1,1,1,1,1,1]

from typing import List

class Solution:
    # time complexity O(N*K) where n is the length of bits and k is K
    # space is O(1) as we operate on the array in place
    def minKBitFlips(self, A: List[int], K: int) -> int:
        def flip_bits(start,end,bits):
            for i in range(start,end):
                # flip the bit at the location
                bits[i] ^= 1

        n = len(A)
        num_flips = 0

        for i in range(n):
            if A[i] == 0:
                # if we go out of bound then we know we cannot flip anymore bits to make it all 1s
                if i+K > n:
                    return -1
                num_flips+=1
                flip_bits(i,i+K,A)
        # if all are true ie 1 then return num flips. sucess branch
        if all(A):
            return num_flips
        else:
            return -1


if __name__ =="__main__":
    mySolution = Solution()
    # bits = [0,1,0]
    # K = 1
    # returns 2
    # print(mySolution.minKBitFlips(bits,K))

    # bits = [1,1,0]
    # K = 2
    # # returns -1
    # print(mySolution.minKBitFlips(bits,K))

    bits = [0,0,0,1,0,1,1,0]
    K = 3
    # returns 3
    print(mySolution.minKBitFlips(bits,K))



















    # notes
