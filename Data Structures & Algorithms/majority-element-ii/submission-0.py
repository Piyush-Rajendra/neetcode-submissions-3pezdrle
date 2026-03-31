from pprint import pprint
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        floor = len(nums) // 3
        pprint(floor)
        count = defaultdict(int)
        out = []
        for n in nums:
            count[n] += 1
        
        for n, freq in count.items():
            if freq > floor:
                out.append(n)
        return out

                


        