class Solution:
    def rob(self, nums: List[int]) -> int: 
        # Tabulation DP
        n = len(nums)
        # if n == 1:
        #     return nums[0]
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))


    def helper(self, nums:List[int])-> int:
        # n = len(nums)
        # dp = [0] * n 

        # if not nums:
        #     return 0
        # if n == 1:
        #     return nums[0]

        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])

        # for i in range(2, n):
        #     dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        # return dp[-1]
        rob1, rob2 = 0, 0
        for n in nums:
            newRob = max(rob2, n + rob1)
            rob1 = rob2
            rob2 = newRob
        return rob2
