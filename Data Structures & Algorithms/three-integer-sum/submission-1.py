class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        k = 0
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) -1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > k:
                    r -= 1
                elif threesum < k:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums [l-1] and l < r:
                        l += 1
        return res
 
        ''' if sort nums array then it becomes easy to work duplicates
            complexity will be 0(n2) cause of the for loop and two while loops
            time complexity to be O(m) where m is the number od triples and n is the length of the given array
        '''


         
        