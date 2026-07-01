class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        lm = m -1
        ln = n -1
        i = m + n - 1

        while ln >= 0:
            if lm >= 0 and nums1[lm] > nums2[ln]:
                nums1[i] = nums1[lm]
                lm -= 1
            else:
                nums1[i] = nums2[ln]
                ln -= 1
            i -= 1
