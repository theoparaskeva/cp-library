# A swap is defined as taking two distinct positions in an array and swapping the values in them.

# A circular array is defined as an array where we consider the first element and the last element to be adjacent.

# Given a binary circular array nums, 
# return the minimum number of swaps required to group all 1's present in the array together at any location.

 
# Example 1:

# Input: nums = [0,1,0,1,1,0,0]
# Output: 1
# Explanation: Here are a few of the ways to group all the 1's together:
# [0,0,1,1,1,0,0] using 1 swap.
# [0,1,1,1,0,0,0] using 1 swap.
# [1,1,0,0,0,0,1] using 2 swaps (using the circular property of the array).
# There is no way to group all 1's together with 0 swaps.
# Thus, the minimum number of swaps required is 1.
from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ### the length of the final array will be equal to the amount of 1s
        k = nums.count(1)
        l = 0
        mn = 10**5
        c = 0
        ### to deal with the circularity of the array we append it to itself
        nums = nums+nums
        for r in range(len(nums)):
            ### we count the amount of zeroes
            if nums[r] == 0:
                c+=1

            ### when the window reaches the necessary size we slide the window 
            while r-l+1 > k:
                ### keeping track of amount of zeroes in the window
                if nums[l] == 0:
                    c-=1
                
                l+=1
            

                ### keeping track of the smallest amount of 0s in the array
                mn = min(mn,c)
            
        
        return mn
