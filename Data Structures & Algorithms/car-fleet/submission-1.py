class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        stack = []

        for i in range(len(pair)):
            pos, speed = pair[i]
            relativeTime = ((target - pos) / speed)
            stack.append(relativeTime)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
        
        