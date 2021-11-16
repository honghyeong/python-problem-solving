# 121

# Brute Force Algorithm
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_price=0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                max_price=max(max_price,prices[j]-prices[i])
        return max_price
        
        
# Kadane's algorithm
import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        min_price=sys.maxsize

        # renew min, max:
        for price in prices:
            min_price=min(min_price,price)
            profit=max(profit,price-min_price)
            
        return profit
