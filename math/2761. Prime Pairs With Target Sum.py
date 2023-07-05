# You are given an integer n. We say that two integers x and y form a prime number pair if:

# 1 <= x <= y <= n
# x + y == n
# x and y are prime numbers
# Return the 2D sorted list of prime number pairs [xi, yi]. 
# The list should be sorted in increasing order of xi. If there are no prime number pairs at all, return an empty array.

# Note: A prime number is a natural number greater than 1 with only two factors, itself and 1.

 # Example 1:

# Input: n = 10
# Output: [[3,7],[5,5]]
# Explanation: In this example, there are two prime pairs that satisfy the criteria. 
# These pairs are [3,7] and [5,5], and we return them in the sorted order as described in the problem statement.
from typing import List
from math import isqrt

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        if n <= 2:
            return([])
        
        ### Sieve to create array of all prime numbers in range n
        prime = [True] * n
        prime[0] = False
        prime[1] = False

        for i in range(2,isqrt(n)+1):
            if prime[i]:
                for x in range(i*i, n, i):
                    prime[x] = False
        
        ans = []
        ### loop through n checking both x and n-x are prime, stopping halfway to avoid repeat pairs
        for x in range(2,n):

            if x+x > n:
                break
            if prime[x] and prime[n-x]:
                ans.append([x,n-x])
            
            
               
        
        return ans
        