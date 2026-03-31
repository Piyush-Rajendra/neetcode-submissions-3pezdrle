class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # maxProd = nums[0]

        # for i in range(len(nums)):  # 1
        #     curr = nums[i] #1
        #     maxProd = max(curr, maxProd) # 1
        #     for j in range(i+1,  len(nums)): # 2 -3 4
        #         curr *= nums[j] #2 -3 4
        #         maxProd = max(maxProd, curr) #2 2 4 
        # return maxProd
        res = nums[0]
        maxCurr, minCurr = 1, 1

        for n in nums:
            temp = n * maxCurr
            maxCurr = max(n * maxCurr, n * minCurr, n)
            minCurr = min(temp, n * minCurr, n)
            res = max(res, maxCurr)
        return res