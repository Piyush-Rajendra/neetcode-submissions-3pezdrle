class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):  # Different lengths can't be anagrams
        #     return False

        # hashmapS, hashmapT = {}, {}  # Character frequency maps for both strings

        # for ch in s:  # Count character frequencies in s
        #     hashmapS[ch] = 1 + hashmapS.get(ch, 0)
        # for ch in t:  # Count character frequencies in t
        #     hashmapT[ch] = 1 + hashmapT.get(ch, 0)
        # for ch in hashmapS:  # Compare frequency counts
        #     if hashmapS[ch] != hashmapT.get(ch, 0):  # Mismatch found
        #         return False

        # return True  # All frequencies match


        hashMap = {}
        if not len(s) == len(t):
            return False
        for i in range(len(s)):
            hashMap[s[i]] = 1 + hashMap.get(s[i], 0)
        
        for i in range(len(t)):
            if t[i] in hashMap:
                hashMap[t[i]] -= 1
                if hashMap[t[i]] < 0:
                    return False
            else:
                return False
        return True
        


