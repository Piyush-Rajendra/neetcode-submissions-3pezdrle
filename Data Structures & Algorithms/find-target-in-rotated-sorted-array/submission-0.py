class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m
            
            # Determine which half is sorted
            if nums[l] <= nums[m]:  # Left half is sorted
                if nums[l] <= target < nums[m]:  # Target in sorted left half
                    r = m - 1
                else:  # Target in right half
                    l = m + 1
            else:  # Right half is sorted
                if nums[m] < target <= nums[r]:  # Target in sorted right half
                    l = m + 1
                else:  # Target in left half
                    r = m - 1
        
        return -1