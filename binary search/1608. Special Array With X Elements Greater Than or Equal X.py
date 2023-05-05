# You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that 
# there are exactly x numbers in nums that are greater than or equal to x.

# Notice that x does not have to be an element in nums.

# Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

 

# Example 1:

# Input: nums = [3,5]
# Output: 2
# Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.
from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        
        def binary(x):
            nums.sort()
            l,r = 0,len(nums)
            
            while l<r:
                mid = (l+r) //2
                if nums[mid] >= x:
                    r = mid
                else:
                    l = mid+1
            return len(nums) - r 
        
        for y in range(max(nums)+1):
            if y == binary(y):
                return y
        return -1
    


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(105):
            c = 0
            for x in nums:
                if x >= i:
                    c += 1
            if c == i:
                return c
        return -1
            
        
            