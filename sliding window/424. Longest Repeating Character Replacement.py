# You are given a string s and an integer k. You can choose any character of the string 
# and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        ans = 0
        l = 0
        for r in range(len(s)):
            ### count each letter
            count[s[r]] +=1
            
            ### we can replace at most k letters so as soon as the length of the list minus the most frequent letter is more than k 
            # our window is not viable
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -=1
                l+=1
            
            ### keeping track of the max window length
            ans = max(ans,r-l+1)
        return ans