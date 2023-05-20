# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow = {"a","e","i","o","u"}
        ### set l to 0, the first element in our window
        l,c,ans = 0,0,0


        for r in range(len(s)):
            ## loop through and if current letter is a vowel, increment the count
            if s[r] in vow:
                c+=1
            ## once we reach the size of our window
            if r - l + 1 > k:
                ## if the first letter we counted was a vowel we decrement the count
                if s[l] in vow:
                    c-=1
                ## we now move the window along by incrementing the left pointer
                l+=1
            ## in each iteration we check if the current count of vowels in our window has increased
            ans = max(ans,c)
        
        return ans
        
        
