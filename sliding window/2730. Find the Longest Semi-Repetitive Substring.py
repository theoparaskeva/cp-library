# You are given a 0-indexed string s that consists of digits from 0 to 9.

# A string t is called a semi-repetitive if there is at most one consecutive pair of the same digits inside t.

# Return the length of the longest semi-repetitive substring inside s.

# A substring is a contiguous non-empty sequence of characters within a string.

 

# Example 1:

# Input: s = "52233"
# Output: 4
# Explanation: The longest semi-repetitive substring is "5223", which starts at i = 0 and ends at j = 3. 


class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        l = 0
        mx = 1 
        c = 0
        
        ### set range from 1,length of s
        for r in range(1,len(s)):
            ### if consecutive pair we increment count
            if s[r] == s[r-1]:
                c+=1
            ### if we have more than one consecutive pair
            if c>1:
                ### we keep looping until we can remove one of the numbers of the pair
                if s[l] == s[l+1]:
                    c-=1
                l+=1
            ### keeping check of largest substring
            mx = max(mx,(r-l)+1)
        
        return mx
        