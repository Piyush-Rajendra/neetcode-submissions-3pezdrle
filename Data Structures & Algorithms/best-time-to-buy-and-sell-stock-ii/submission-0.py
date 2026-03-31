class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        buy and sell on same day
        can do number of transactions but can hold only one share at a time
        need to find maximum profit that can be achieved, if there are is no profit at that time return zero
        no need to check for loss
        so use greedy approach such as:
        use single pointer i that  goes till end of len(prices)but starts from 1:
        then check if prices[i] > prices[i -1]:
        profit += prices[i] - prices[i - 1]

        return profit
        '''

        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i -1]:
                profit += (prices[i] - prices[i - 1])
        return profit



        