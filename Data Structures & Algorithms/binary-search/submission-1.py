class Solution:
    def binary_search(self, l:int, r:int, nums:List[int], target: int) -> int:

        if l > r:
            return -1
        m = l + (r-l) // 2

        if nums[m] == target:
            return m
        if nums[m] < target:
            return self.binary_search(m + 1, r, nums, target)
        return self.binary_search(l, m - 1, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)



        '''
        we have sorted nums array goal is to find target element index in log n time,
        to do that binary search approach is a good fit recursive one and iterative one are the two approaches where we use l and r pointers
        in the start l will be zero and r will be the  end index of the nums array so len(nums) - 1 

        take the middle element by m = l + (r-l) // 2compare if that number is smaller than or greater to the target
        and recursively call binary function again but manager l and r pounters accordingly.
        also need to check before starting or calculating the mid is to look for l < r if this is the case return -1 
        '''


        