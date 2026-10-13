# ==========================================================
# 121. Best Time to Buy and Sell Stock
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 155 ms (Beats 7%)
# Memory     : 19.8 MB (Beats 15%)
# Link       : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# ==========================================================

class Solution(object):
    def maxProfit(self, prices):
        if prices == sorted(prices, reverse = True):
            return 0
        min = prices[0]
        profit = 0
        for i in range(0,len(prices)):
            if prices[i] < min:
                min = prices[i]
         
            if (prices[i] - min) > profit:
                profit = prices[i] - min

        return profit

      
        return profit
        