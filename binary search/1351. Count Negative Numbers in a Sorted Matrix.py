# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

# Example 1:

# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:

# Input: grid = [[3,2],[1,0]]
# Output: 0
from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def binary(row):
            l,r = 0,len(grid[0])
            while l<r:
                mid = (l+r )//2
                if row[mid] < 0:
                    r = mid
                else:
                    l = mid+1
            return len(grid[0]) - r
        
        c= 0
        for x in grid:
            c+=binary(x)
        
        return c
            