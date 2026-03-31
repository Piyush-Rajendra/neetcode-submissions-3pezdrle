class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        we are 2 we check if 2 == k if it is we increment res by 1 and also increment both pointers together

        -1 > k now increase one pointer by one and check if sum of -1 and 1 what it is  < k so we increase lets say pointerj again 
        now we check 2 but now we know sum of complete string thats trimmed is > targett so we decrease 
        
        '''
        res = curSum = 0
        prefixSums = { 0 : 1 }

        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        return res
        