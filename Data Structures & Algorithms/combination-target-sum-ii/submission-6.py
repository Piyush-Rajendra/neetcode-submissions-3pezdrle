class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()

        def dfs(index, currentList, total):
            if total == target:
                res.add(tuple(currentList))
                return
            
            if total > target or index >= len(candidates):
                return

            currentList.append(candidates[index])
            dfs(index + 1, currentList, total + candidates[index])
            currentList.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1

            dfs(index + 1, currentList, total)
            
        dfs(0, [], 0)
        return [list(combination) for combination in res]
        