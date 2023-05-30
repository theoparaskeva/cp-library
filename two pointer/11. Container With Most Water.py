# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 
# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section) the container can contain is 49.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        ### pointer at either end of list
        l,r =0 , len(height)-1

        while l <r:
            ### area is equal to size of the current container multiplied by the smaller of the two endpoints
            area = (r-l) * min(height[l],height[r])
            ### keep track of largest area we see
            ans = max(ans,area)

            ## this logic ensures that we possibly increase the size of our container by taking the larger value of our l,r pointers
            # and incrementing/decrementing the smaller
            if height[l] < height[r]:
                l+=1
            
            else:
                r-=1
        return ans
            
            