class Solution:
    # time is o(n) and space is o(1)
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPriceSoFar = prices[0]
        for i in range(len(prices)):
            if prices[i] < minPriceSoFar:
                minPriceSoFar = prices[i]
            else:
                currentProfit = prices[i] - minPriceSoFar
                maxProfit = max(currentProfit, maxProfit)
        return maxProfit
