# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"

s = "hello"
class Solution:
    def reverseVowels(self, s: str) -> str:
        l,r = 0,len(s)-1
        vow = ["a","e","i","o","u","A","E","I","O","U"]
        vow = set(vow)
        s = list(s)
        while l<r:
            if s[l] in vow and s[r] in vow:
                s[l],s[r] = s[r],s[l]
                l+=1
                r-=1
            
            elif s[l] not in vow:
                l+=1
            
            elif s[r] not in vow:
                r-=1
            
            else:
                l+=1
                r-=1
        
        return "".join(s)



