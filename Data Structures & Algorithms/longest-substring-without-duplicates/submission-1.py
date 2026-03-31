class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # charSet = set()
        # l = 0
        # res = 0
        # for r in range(len(s)):
        #     while s[r] in charSet:
        #         charSet.remove(s[l])
        #         l += 1
        #     charSet.add(s[r])
        #     res = max(res, r - l + 1)
        # return res
        '''
        res is going to be an integer that will be length of the longest substirng wihout duplicates chars
        example we have string happy so the longest cont substring will be hap returns len 3 the answer
        2nd case xxx answer here will be 1 because no duplicates 
        can these strings have delimitters or digits? 
        strings can be empty?
        1st approach: 
        res = 0 
        for i in range(len(s)):
            longStr = set()
            for j in range(i, len(s)):
                if s[j] in longStr:
                    break:
                longStr.add[j]
            res = max(res, len(longStr))
        return res
            time complexity should be O (n * m)
        Where 
n is the length of the string and 
m is the total number of unique characters in the string.
    slding window: shrink from left when found duplicate so use a two pointers check if that element already exist in set() simultaneously maintain longest substring lengeth

        '''
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max( res, r - l + 1)
        return res
 