class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        '''
        sort
        and use two pointers one at start one at the end 
        now we try to add them together to check if we are able to create a pair which is less than or equal to the limit
        we increase left pointer if we include it with thte right pointer and right pointer decreases 
        all the time.
        people.sort()
        '''
        left, right  = 0, len(people) - 1
        minimum = 0
        while left <= right:
            if (people[right] + people[left]) <= limit:
                minimum += 1
                left += 1
                right -= 1
            else:
                minimum += 1
                right -= 1
        
        return minimum
        
        