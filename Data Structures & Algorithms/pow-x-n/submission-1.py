class Solution:
    def pow_helper(self, x:float, n:int) -> float:
        if n == 0:
            return 1
        
        half = self.pow_helper(x, n//2 )
        if n % 2 == 0:
            return half * half 
        else:
            return half * half * x

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.pow_helper(x, -n)
        else:
            return self.pow_helper(x, n)