class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()

        def dfs(currentList):
            if len(currentList) == len(nums):
                res.append(currentList[:])
                return

            for i in range(len(nums)):
                if i in visited:  # O(1) lookup
                    continue
                visited.add(i)
                currentList.append(nums[i])
                dfs(currentList)
                currentList.pop()
                visited.remove(i)  # backtrack the set too!

        dfs([])
        return res

        