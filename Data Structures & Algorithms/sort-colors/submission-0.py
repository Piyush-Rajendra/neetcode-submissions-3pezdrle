class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for num in nums:  #creating a hashmap to store count of num in nums
            count[num] +=1  # when encountered add one to the count of that number
        
        index = 0
        for i in range(3):
            while count[i]:    #till count for that number is zero
                count[i] -= 1  #decrement 1 each time
                nums[index] = i # for that index add value of i
                index += 1 #increment index to store next value at different index
