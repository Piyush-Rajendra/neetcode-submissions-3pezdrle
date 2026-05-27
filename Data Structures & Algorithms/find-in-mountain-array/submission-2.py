class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # Find Peak peak = lo
        # binary search on left side return mid
        # binary search on right side return mid
        # return 1

        lo = 0
        hi = mountainArr.length() - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if mountainArr.get(mid) > mountainArr.get(mid + 1):
                hi = mid            
            else:
                lo = mid + 1

        peak = lo
        lo = 0
        hi = peak
        while lo <= hi:
            mid = (lo + hi) // 2
            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        lo = peak + 1
        hi = mountainArr.length() - 1 
        while lo <= hi:
            mid = (lo + hi) // 2
            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) < target:
                hi = mid - 1
            else:
                lo = mid + 1
        

        return -1
