# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# You can return the answer in any order.

 # Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for x in range(len(nums)):
            ### target - current number == the other number needed
            s = target - nums[x]
            ### if our missing number has been seen before we return
            if s in dic:
                return [x,dic[s]]
            ### otherwise we save the number as the key and the index as the value
            else:
                dic[nums[x]] = x