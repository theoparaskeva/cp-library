# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ### initialise defaultdict with list
        dic = defaultdict(list)
      # dic = dict()

        for s in strs:
          ### sort each string so anagrams are equal
          key = "".join(sorted(list(s)))
          ### all anagrams will be appended to a list with the same key
          dic[key].append(s)
        # dic.setdefault(key, []).append(s)

        ### loop through all lists and append to new list
        lis = []
        for l in dic.values():
            lis.append(l)
        
        return lis
