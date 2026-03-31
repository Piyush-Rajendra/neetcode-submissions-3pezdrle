class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()

        i =  0
        while i < len(nums):
            if nums[i] in duplicate:
                return True
            duplicate.add(nums[i])
            i += 1
        return False
    

        