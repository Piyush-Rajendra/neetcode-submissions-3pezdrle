class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        first_word = strs[0]

        for i in range(len(first_word)):
            char = first_word[i]

            for s in strs[1:]:
                if i == len(s) or char != s[i]:
                    return first_word[:i]
        
        return first_word
        