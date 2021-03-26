# Leetcode StoneGameIII
# Alice and Bob continue their games with piles of stones. There are several 
# stones arranged in a row, and each stone has an associated value which is an
# integer given in the array stoneValue.
#
# Alice and Bob take turns, with Alice starting first. On each player's turn,
# that player can take 1, 2 or 3 stones from the first remaining stones in the row.
#
# The score of each player is the sum of values of the stones taken. The score of
# each player is 0 initially.
#
# The objective of the game is to end with the highest score, and the winner is
# the player with the highest score and there could be a tie. The game continues
# until all the stones have been taken.
#
# Assume Alice and Bob play optimally.
#
# Return "Alice" if Alice will win, "Bob" if Bob will win or "Tie" if they end
# the game with the same score.
#
#
#
# Example 1:
#
# Input: values = [1,2,3,7]
# Output: "Bob"
# Explanation: Alice will always lose. Her best move will be to take three piles
# and the score become 6. Now the score of Bob is 7 and Bob wins.


from typing import List
class Player:
    def __init__(self,name):
        self.name = name
        self.score = 0

class Solution:
    # returns who wins
    # this works for positive numbers only
    # def stoneGameIII(self, stoneValue: List[int]) -> str:
    #     alice = Player("Alice")
    #     bob = Player("Bob")
    #     players = []
    #     players.append(alice)
    #     players.append(bob)
    #     player_index,best_index,i=0,0,0
    #     while i< len(stoneValue):
    #         j = i+ 3
    #         cmax = float("-inf")
    #         while j > i:
    #             if j > len(stoneValue):
    #                 j-= 1
    #                 continue
    #             csum = sum(stoneValue[i:j])
    #             if csum > cmax:
    #                 cmax = csum
    #                 best_index = j
    #             j -= 1
    #         i = best_index
    #         players[player_index].score+= cmax
    #         player_index^=1
    #     if players[0].score > players[1].score:
    #         return players[0].name
    #     elif players[1].score > players[0].score:
    #         return players[1].name
    #     else:
    #         return "Tie"
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        suffix_sum = [0 for _ in range(n + 1)]
        # dp[i] - maximum sum a player can accumulate he/she starts at position i
        dp = [0 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            suffix_sum[i] = stoneValue[i] + suffix_sum[i+1]
        # suffix_sum: [10, 9, 7, 4, 0]

        for i in range(n - 1, -1, -1):
            player_pick_two_stones, player_pick_three_stones = float('-inf'), float('-inf')
            # always have to pick at least one
            player_pick_one_stone = stoneValue[i] + suffix_sum[i + 1] - dp[i + 1]
            # pick two stone
            if i + 1 < n:
			    # suffix_sum[i] = stoneValue[i] + stoneValue[i + 1] + suffix_sum[i + 2]
                player_pick_two_stones = suffix_sum[i] - dp[i + 2]
            # pick three stone
            if i + 2 < n:
			    # suffix_sum[i] = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] + suffix_sum[i + 3]
                player_pick_three_stones = suffix_sum[i] - dp[i + 3]
            print(player_pick_one_stone,player_pick_two_stones,player_pick_three_stones)
            dp[i] = max(player_pick_one_stone, player_pick_two_stones, player_pick_three_stones)
        print(dp)
        print(suffix_sum)
        if 2 * dp[0] == suffix_sum[0]:
            return 'Tie'
        elif 2 * dp[0] > suffix_sum[0]: # Alice score > Bob's score, dp[0] > suffix_sum[0] - dp[0]
            return 'Alice'
        else:
            return 'Bob'


if __name__ =="__main__":
    mySolution = Solution()
    stones = [1,2,3,4]
    print(mySolution.stoneGameIII(stones))
