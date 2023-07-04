# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ### counter with each letter of s1
        c = Counter(s1)
        n = len(s1)

        l = 0 
        for r in range(len(s2)):
            ### if letter is in our substring we minus it from the counter
            if s2[r] in c:
                c[s2[r]] -=1
            
            ### our window will be equal to the size of s1 
            while r-l+1 > n:
                ### if start of window is in c, as we move the window we remove it by adding it back to the counter
                if s2[l] in c:

                    c[s2[l]] +=1
                l+=1
            ### each iteration, we check if all Counts of letter in s1 are equal to 0 
            # meaning that our current window is equal to our s1 substring
            if all([c[x] == 0 for x in c]):
                return True
                
            
            
        return False
