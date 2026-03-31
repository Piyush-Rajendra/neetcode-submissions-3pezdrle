'''
We use bottom-up dynamic programming, where
dp[i] means: can the substring s[i:] be segmented using wordDict.
We initialize dp[len(s)] = True because an empty string is already valid.
We iterate from the end of the string to the start.
At each index i, we try every word w in wordDict:
If s[i : i + len(w)] == w and
dp[i + len(w)] is True,
then dp[i] = True and we stop checking further words.
Finally, we return dp[0], which tells us whether the entire string can be segmented.
time Complexity: O(n*m*t)
space complexity: O(n)
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) -1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]

        