class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        '''
        sort
        and use two pointers one at start one at the end 
        now we try to add them together to check if we are able to create a pair which is less than or equal to the limit
        we increase left pointer if we include it with thte right pointer and right pointer decreases 
        all the time.
        people.sort()
        '''
        people.sort()
        left, right, res  = 0, len(people) - 1, 0
        while left <= right:
            remain = limit - people[right]
            right -= 1
            res += 1
            if left <= right and remain >= people[left]:
                left += 1
        return res
        
        