class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def expand(left: int, right: int) -> int:
            curr_count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                curr_count += 1
                left -= 1
                right += 1
            return curr_count

        for i in range(len(s)):
            count += expand(i, i)
            count += expand(i, i + 1)

        return count
        
                  


    #     '''
    #    I have a string and I need to find count of numberof substrings that are palindrome
    #    check for paliindromes and count them 
       
    #    '''