class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i, num in enumerate(nums):
            if num == val:
                nums[i] = 51
        k = 0
        for num in nums:
            if num <= 50:
                k += 1
        nums.sort()
        return k
        