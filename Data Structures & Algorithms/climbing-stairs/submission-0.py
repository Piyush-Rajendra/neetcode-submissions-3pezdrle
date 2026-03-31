''' Memoization approach
        store step and value in hashmap, in function check if n is hashmap if yes then return
        check base cases : n =1 n =2 then use recursion to store values with steps'''
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def helper(n):
            if n in memo:
                return memo[n]
            if n == 1: return 1
            if n == 2: return 2
            
            memo[n] = helper(n-1) + helper(n-2)
            return memo[n]
        
        return helper(n)

       
