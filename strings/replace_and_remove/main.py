# 6.4 REPLACE AND REMOVE
# Consider the following two rules that are to be applied to an array of characters.
# • Replaceeach'a'bytwo'd's.
# • Delete each entry containing a 'b',

# Method:
# We can combine these two approaches to get a complete algorithm.
# First, we delete 'b's and compute the final number of valid characters of the
# string, with a forward iteration through the string. Then we replace each
# 'a' by two 'd's, iterating backwards from the end of the resulting string.
# If there are more 'b's than 'a's, the number of valid entries will decrease,
# and if there are more 'a's than 'b's the number will increase.
# Tiem complexity O(n) space O(1)
from typing import List
class Solution():
    def replace_and_remove(self,size: int, s: List[str]) -> int:
        # Forward through the array counting a's and dropping b's
        a_count,write_idx = 0,0
        for i in range(size):
            if s[i] != 'b':
                s[write_idx] = s[i]
                write_idx += 1
            if s[i] == 'a':
                a_count += 1
        # Loop 1 (a)
        # write_idx = 0 a_count = 0
        # Loop 2 (b)
        # write_idx =1 a_count =1 [a,b,c,a,b,c]
        # Loop 3 (c)
        # write_idx =1 a_count = 1 [a,c,c,a,b,c]
        # Loop 4 (a)
        # write_idx = 2 a_count = 1 [a,c,a,a,b,c]
        # Loop 5 (b)
        # write_idx 3 = a_count = 2 [a,c,a,a, b,c]
        # Loop 6
        # write_idx 3 = a_count = 2 [a,c,a,c,b,c]
        # write_idx = 4 a_count = 2



        # backward iteration repalcing a's with 'dd'
        cur_idx = write_idx-1
        # cur_idx = 4-1 ==>3
        write_idx += a_count -1
        # write_idx = 4+2-1 ==> 4
        final_size = write_idx + 1
        while cur_idx >= 0:
            if s[cur_idx] == 'a':
                s[write_idx -1:write_idx + 1] = 'dd'
                write_idx -= 2
            else:
                s[write_idx] = s[cur_idx]
                write_idx -= 1
            cur_idx -= 1

        # Loop 1
        # s[cur_idx] =='a'  'c' =='a' False
        #  [a,c,a,c,c,c]
        # Loop 2
        # cur_idx 2 >=0 ==> True
        # 'a' =='a' ==> True
        # [a,c,d,d,c,c]
        # cur_idx = 1 write_idx 1
        # Loop 3 cur_idx 1 >=0 ==> True
        # [a,c,c,d,d,c]
        # [d,d,c,d,d,c]
        print(s)
        return final_size




if __name__ == "__main__":
    mySolution = Solution()
    print(mySolution.replace_and_remove(6,['a','b','c','a','b','c']))
