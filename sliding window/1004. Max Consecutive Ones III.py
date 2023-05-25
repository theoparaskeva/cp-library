# Given a binary array nums and an integer k, return the maximum number of consecutive 1's 
# in the array if you can flip at most k 0's.

#  Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

from typing import List
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        l,ans,z,c = 0,0,0,0
        for x in range(len(A)):
            # count ones and possible flipped zeroes
            c+=1
            # count each zero
            if A[x] == 0:
                z+=1
            # if count of zeroes is more than K, current subarray is not viable
            while z>K:
                ## if the first item in our window is 0, array is viable again, if not we increment until it is
                if A[l] == 0:
                    z-=1
                ### decrement our counter each time we remove a number from the subarray
                c-=1
                
                ### increment our left pointer until we break out of while loop
                l+=1
            
            ### store our largest subarray
            ans = max(ans,c)
        
        return ans
        