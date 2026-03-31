class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ''' profit = 0
        return highest profit, that is purchase when stock is low and sell when 
            
                profit = 0

        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1, len(prices)):
                sell = prices[j]
                profit = max (profit, sell - buy )
        return profit

        O(n^2) and O(1)
        
         '''

        l, r = 0, 1
        profit = 0
        maxP = 0

        while r < len(prices):
            if prices[l] < prices [r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP