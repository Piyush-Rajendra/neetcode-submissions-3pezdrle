class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                skipLeft = s[left + 1: right + 1]   #skip left index and go on till right ( right is exclusive so we do + 1)
                skipRight = s[left: right]  #skip right and go from left to right
                return (skipLeft == skipLeft[::-1] or skipRight == skipRight[::-1])
            
            left += 1
            right -= 1
        return True


        