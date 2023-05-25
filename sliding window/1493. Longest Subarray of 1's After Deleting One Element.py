# 1493. Longest Subarray of 1's After Deleting One Element
# Medium
# 1.6K
# 31
# Companies
# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. 
# Return 0 if there is no such subarray.

 # Example 1:

# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l,c,d,ans = 0,0,0,0
        ### we have to delete a number even if list is all ones
        if sum(nums) == len(nums):
            return sum(nums)-1
        

        for r in range(len(nums)):
            ### count all zeroes
            if nums[r] == 0:
                c+=1
            ### count ones
            else:
                d+=1
            ### if count of zeroes is more than two, array is not viable as we can only delete one
            while c >= 2:
                ### if our left pointer is zero, array is viable again so we decrement our zero counter
                if nums[l] == 0:
                    c-=1
                ### if it is equal to 1 we decrement the count of our subarray
                else:
                    d -=1
                ### increment left pointer until we break out of while loop
                l+=1
            ### store largest subarray
            ans = max(ans,d)

            
           
        return ans
