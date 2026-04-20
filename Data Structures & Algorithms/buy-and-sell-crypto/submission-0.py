class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        profit = 0

        for i in range(1,len(prices)):
            if prices[i]-prices[buy] > profit:
                sell = i
                profit = prices[i]-prices[buy]
            else:
                if prices[i]< prices[buy]:
                    buy = i


        return profit
