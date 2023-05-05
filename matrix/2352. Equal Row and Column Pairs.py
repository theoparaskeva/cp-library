# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        y = [list(a) for a in zip(*grid)]
        c = 0
        for x in range(len(grid)):
            c += y.count(grid[x])

        return c
