class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """ """
        res = []

        def dfs(index, currentList, total):
            if total == target:
                res.append(currentList[:])
                return

            if index >= len(nums) or total > target:
                return

            for i in range(index, len(nums)):
                currentList.append(nums[i])
                dfs(i, currentList, nums[i] + total)
                currentList.pop()
                
        dfs(0, [], 0)
        return res
