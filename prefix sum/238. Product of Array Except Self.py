# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lp = [1]*len(nums)
        rp = [1]*len(nums)

        output = [0]*len(nums)

        for i in range(1, len(nums)):
            lp[i] = lp[i-1] * nums[i-1]

        for j in range(len(nums)-2, -1, -1):
            rp[j] = rp[j+1] * nums[j+1]

        for x in range(len(nums)):
            output[x] = rp[x] * lp[x]

        return output
