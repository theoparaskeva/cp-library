# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ## create a set
        s = set(nums)
        ans = 0

        ## loop through each number
        for x in nums:
            ## to find the first number of the sequence we check untill we cant find a number before
            if x - 1 not in s:
                ## reset for each sequence
                l = 0
                ## keep checking if sequence continues by incrementing l 
                while x+l in s:
                    l+=1
                ## keep track of largest sequence
                ans = max(ans,l)
        
        return ans