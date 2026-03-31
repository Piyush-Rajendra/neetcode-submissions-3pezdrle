class Solution:
    def isValid(self, s: str) -> bool:
        # goal is to use stack such that whenever we get a closing bracket it is for the top most items
        # if thats not the case we return False
        # if its an opening bracket we append it.
        # brute force approach we can
        stack = []
        cTo = {"}":"{", "]":"[", ")":"("}

        for i in s:
            if i in cTo:
                if stack and stack[-1] == cTo[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return True if not stack else False




