class Solution(object):
    def maxProfit(self, prices):

        if len(prices) == 0:
            return 0

        maxProfit = 0
        minPrice = prices[0]

        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            if prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice

        return maxProfit







print(Solution().maxProfit([1,2,11,0,4,7]))