# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

#  Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        ### length of the entire matrix
        n = len(matrix)
        ### length of each row in matrix
        m = len(matrix[0])

        ### binary function takes row (current row of matrix)
        def binary(row):
            ## pointers at either end of list
            l,r = 0,m-1
            while l<=r:
                ### middle of list initially 
                mid = (r+l) //2
                ### if mid is equal to target we can return true
                if matrix[row][mid] == target:
                    return True
                ### if it is larger we know it will be in the first half of the list so we set our right pointer to the current 
                # mid -1 
                elif matrix[row][mid] > target:
                    r = mid-1
                ### if it is smaller we know target is in second half so we set our left to mid+1
                else:
                    l = mid+1
            return False
        
        ### loop through each row in matrix and check if our target appears in any
        for x in range(n):
            if binary(x):
                return True
        ### if not we return false
        return False