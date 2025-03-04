#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price=prices[0]
        sell_price=0
        profit=0
        for day in range(1,len(prices),1):
            if prices[day] < buy_price:
                if sell_price-buy_price > profit:
                    profit=sell_price-buy_price
                sell_price=0
                buy_price=prices[day]
            elif prices[day] > sell_price:
                sell_price=prices[day]
            if day == len(prices)-1 and sell_price-buy_price > profit:
                profit=sell_price-buy_price
        
        if profit < 0:
            return 0
        else:
            return profit
# @lc code=end

