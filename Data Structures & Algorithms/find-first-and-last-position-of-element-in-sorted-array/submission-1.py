class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(findFirst: bool) -> int:
            l, r, idx = 0, len(nums) - 1, -1
            while l <= r:
                mid = r + l // 2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    idx = mid
                    if findFirst:
                        r = mid - 1
                    else:
                        l = mid + 1
            return idx
        return [binarySearch(True), binarySearch(False)]
        # res = [-1, -1]
        # for i,n in enumerate(nums):
        #     if n == target:
        #         if res[0] == -1:
        #             res[0] = i
        #         res[1] = i
        # return res
        