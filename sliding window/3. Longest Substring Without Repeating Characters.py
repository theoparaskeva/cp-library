# Given a string s, find the length of the longest 
# substring
#  without repeating characters.
# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = defaultdict(int)
        l,ans = 0,0
        for r in range(len(s)):
            # increment in dic for every instance of letter
            dic[s[r]] +=1
            # while we have more than one instance of character in substring
            while dic[s[r]] > 1:
                # remove characters until we have a viable substring
                dic[s[l]] -=1
                l+=1
            
            # store max substring length
            ans = max(ans,(r-l)+1)
        
        return ans
                
            