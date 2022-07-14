from typing import List


class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        g = {}
        indeg = [0] * n
        # for i in range(m):
        #     for j in range(n):

