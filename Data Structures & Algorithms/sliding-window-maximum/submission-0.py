class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        for i in range(len(nums) - k + 1):
            maxWindow = nums[i]
            for j in range(i, i + k):
                maxWindow = max(maxWindow, nums[j])
            output.append(maxWindow)
        
        return output
        