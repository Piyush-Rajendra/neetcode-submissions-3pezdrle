class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0: # right aestroid is smaller tha left one so it gets destroyed 
                    stack.pop()
                elif diff > 0: # right aestroid is bigger than left one so it never crosses 
                    a = 0
                else: # if diff = 0 that is same value both asteroids get destroyed
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
        return stack
             
        