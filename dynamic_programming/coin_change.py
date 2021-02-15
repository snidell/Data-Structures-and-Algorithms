# Leetcode 322 Coin Change
# You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need to
# make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
#
# You may assume that you have an infinite number of each kind of coin.

# exampleInput: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

from typing import List

class Solution:
    def coinChange(self,coins: List[int],amount:int)-> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin,amount+1):
                dp[x] = min(dp[x],dp[x-coin]+1)
        return dp[amount] if dp[amount] != float('inf') else -1


if __name__ =="__main__":
    mySolution = Solution()
    print(mySolution.coinChange([1,2,5],12))
    # dp
    # 1             [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12]
    # 2             [0, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    # 5             [0, 0, 0, 0, 0, 1, 2, 2, 3, 3, 2, 3, 3]
    # min() above   [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3, 3]
