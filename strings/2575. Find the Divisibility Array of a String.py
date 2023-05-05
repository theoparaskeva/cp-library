# You are given a 0-indexed string word of length n consisting of digits, and a positive integer m.

# The divisibility array div of word is an integer array of length n such that:

# div[i] = 1 if the numeric value of word[0,...,i] is divisible by m, or
# div[i] = 0 otherwise.
# Return the divisibility array of word.


# Example 1:

# Input: word = "998244353", m = 3
# Output: [1,1,0,0,0,1,1,0,0]
# Explanation: There are only 4 prefixes that are divisible by 3: "9", "99", "998244", and "9982443".

from typing import List
class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        l,p = [0]*len(word),0
        for x in range(len(word)):
            print((10 * p + ord(word[x]) - ord('0')))
            p = (10 * p + ord(word[x]) - ord('0')) % m
            if not p:
                l[x] =1
        return(l)
        