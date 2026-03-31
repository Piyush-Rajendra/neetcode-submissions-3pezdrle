class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        maximum in betwee two bars where max = smallest height[i] in between these two pointers
        and we take product of same that is smallest * smallest and we add thsi to max.
        this is one of the approach

        '''
        maxArea = 0

        l, r = 0, len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            maxArea = max(maxArea, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea

        