# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in 
# the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        mx = 0
        while r < len(prices):
            ### if left price is less than right price we keep check of total profit
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                mx = max(mx,profit)
            ### if we find a new smallest number we set out left pointer to it
            else:
                l = r
            ### each iteration we will increase r by 1
            r+=1
        return mx
        