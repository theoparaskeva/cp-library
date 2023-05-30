# Given an integer array nums of length n and an integer target, find three integers in 
# nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = 9999999
        ## sort list
        nums.sort()

        for x in range(len(nums)):
            ## set pointers to number after x and last number
            l,r = x+1,len(nums)-1
            while l<r:
                ## current triplet
                tri = (nums[x],nums[l],nums[r])
                ## sum of current triplet
                s = sum(tri)
                ### keep track of closest triplet to target
                if abs(s-target) < abs(ans-target):
                    ans = s
                ## if triplet sum is more than target, we decrement our last pointer 
                if s > target:
                    r-=1
                ## if smaller than target, we increment our left pointer, leading to a larger sum
                elif s < target:
                    l+=1
                else:
                    return target
                
            
        return ans
