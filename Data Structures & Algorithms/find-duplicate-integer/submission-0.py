class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numMap = {}

        for i in range(len(nums)):
            if nums[i] not in numMap:
                numMap[nums[i]] =+ 1
            else:
                return nums[i]

