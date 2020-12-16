class Solution:
    # time complexity O(n) time O(1) space
    def buy_sell_stock(self,prices:[float])->float:
        min_price_so_far, max_profit = float('inf'), 0.0
        for price in prices:
            max_profit_sell_today = price - min_price_so_far
            max_profit = max(max_profit, max_profit_sell_today)
            min_price_so_far = min(min_price_so_far, price)
        return max_profit

    def buy_sell_2(self,prices:[float])-> float:
        max_profit,current_min,current_max= 0.0,float('inf'),float('-inf')
        for i in range(len(prices)):
            current_min = min(current_min,prices[i])
            current_max = max(current_max,prices[i]) # wrong here
            max_profit = max(max_profit,(current_max-current_min))
            print("current_min: ",current_min,"current_max: ",current_max,"max_profit: ",max_profit)
        return max_profit


if __name__ == "__main__":
    mySolution = Solution()
    A = [310,315,275,295,260,270,290,230,255,250]
    print(mySolution.buy_sell_stock(A))
    print(mySolution.buy_sell_2(A))
