# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

# Return a list answer of size 2 where:

# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.

# Note:

# You should only consider the players that have played at least one match.
# The testcases will be generated such that no two matches will have the same outcome.

from typing import List
from collections import defaultdict


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        dic = defaultdict(int)
        w, l = [], []

        for i, j in matches:
            dic[i] += 0
            dic[j] += 1

        for x, y in dic.items():
            if y == 0:
                w.append(x)
            if y == 1:
                l.append(x)

        return [sorted(w), sorted(l)]
