# Given a 1-indexed array of integers numbers that is already sorted in 
# non-decreasing order, find two numbers such that they add up to a specific 
# target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

 
# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ### left pointer at 0, right pointer at end of list
        l ,r = 0, len(numbers)-1


        while l<r:
            ### if both of our pointers equal target
            if numbers[l] + numbers[r] == target:
                ## we have to return the index +1 
                return [l+1,r+1]
            
            ### because list is sorted, If our pointers are greater than our target we decrease our sum by lowering 
            ##  right pointer
            elif numbers[l] + numbers[r] > target:
                r-=1
            
            ## else if we are below target we increase the sum by incrementing our left pointer
            else:
                l+=1
            