class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]

        for i in range(len(nums)):
            curr = nums[i]
            maxProd = max(curr, maxProd)
            for j in range(i+1,  len(nums)):
                curr *= nums[j]
                maxProd = max(maxProd, curr)
        return maxProd