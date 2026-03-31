class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Track opening brackets in order
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }  # Map closing -> opening bracket

        # Example: s = "({[]})"
        # Step 1: c='(' → opening bracket → stack=['(']
        # Step 2: c='{' → opening bracket → stack=['(','{']
        # Step 3: c='[' → opening bracket → stack=['(','{','[']
        # Step 4: c=']' → closing bracket, stack[-1]='[' matches → pop → stack=['(','{']
        # Step 5: c='}' → closing bracket, stack[-1]='{' matches → pop → stack=['(']
        # Step 6: c=')' → closing bracket, stack[-1]='(' matches → pop → stack=[]
        # Result: stack is empty → return True

        for c in s:  # Process each character
            if c in closeToOpen:  # Current char is closing bracket
                if stack and stack[-1] == closeToOpen[c]:  # Check if matches most recent opening
                    stack.pop()  # Valid pair found, remove opening bracket
                else:
                    return False  # Mismatch or no opening bracket available
            else:
                stack.append(c)  # Opening bracket, add to stack
        return True if not stack else False  # Valid only if all brackets matched (empty stack)

