class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        q = deque()
        for i, num in enumerate (nums):
            res.append(num)
            q.append(num)
        
        while q:
            element = q.popleft()
            res.append(element)
        
        return res

            
            
        