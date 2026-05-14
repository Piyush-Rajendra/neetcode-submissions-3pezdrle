class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        def dfs(index, currentList):
            if index == len(nums):
                res.add(tuple(currentList))
                return
            
            for i in range(index, len(nums)):
                currentList.append(nums[i])
                dfs(i + 1, currentList)
                currentList.pop()
                dfs(i + 1, currentList)
            
        dfs(0, [])
        return [list(subset) for subset in res]

        