# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

 # Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
from typing import List

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        ans = [0]* len(temp)

        for x in range(len(temp)):
            ### While we have a number on the stack and the current temp is more than items in the stack
            while stack and temp[x] > stack[-1][0]:
                ### pop off the stack
                t,i = stack.pop()
                ### take the index of the popped temp and subtract it from the current index(first greater temp)
                ans[i] = (x - i)
            ### append each temp and its index
            stack.append([temp[x],x])
        
        return ans
        
        
        