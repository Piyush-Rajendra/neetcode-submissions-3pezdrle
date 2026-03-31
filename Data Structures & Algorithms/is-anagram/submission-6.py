class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmapS, hashmapT = {}, {}

        # build frequency maps
        for ch in s:
            hashmapS[ch] = 1 + hashmapS.get(ch, 0)
        for ch in t:
            hashmapT[ch] = 1 + hashmapT.get(ch, 0)

        # compare counts
        for ch in hashmapS:
            if hashmapS[ch] != hashmapT.get(ch, 0):
                return False

        return True
