class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(index, currentList):
            res.append(currentList[:])
            
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
            
                currentList.append(nums[i])
                dfs(i + 1, currentList)
                currentList.pop()
            
        dfs(0, [])
        return res

        