class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        reverse -> reverse by manipulation of the nums array      
        """
        if k == 0:
            return nums
        k %= len(nums)
        l, r = 0, len(nums) - 1

        def reverse(l, r, nums):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, len(nums) -1, nums)
        reverse(0, k - 1, nums)
        reverse(k, len(nums) -1 , nums)


        
        