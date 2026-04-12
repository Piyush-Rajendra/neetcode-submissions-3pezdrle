class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h = hours = 0
        # piles = list = pile[i] = number of bananas in the pile
        # k is what we need to find which is min time to eat all bananas and if exceed 1 hour it takes next hour too
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            
            if hours <= h:
                res = min(res, k)
                r = k-1
            else:
                l = k + 1
        
        
        return res

        