from typing import List

#solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minBuyPrice = prices[0]
        maxProfit = 0
        for i in range(n):
            if i>0:
                maxProfit = max(maxProfit,prices[i]-minBuyPrice)
                minBuyPrice = min(minBuyPrice,prices[i])
        return maxProfit

#testcase
print(Solution().maxProfit([1,2,3,4,5]))

