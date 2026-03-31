class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmapS, hashmapT = {}, {}

        # count frequencies directly by iterating over characters
        for ch in s:
            hashmapS[ch] = 1 + hashmapS.get(ch, 0)
        for ch in t:
            hashmapT[ch] = 1 + hashmapT.get(ch, 0)

        # compare both hashmaps
        return hashmapS == hashmapT
