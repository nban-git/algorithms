import heapq
from collections import deque
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False for _ in range(n)] for _ in range(n)]
        hq = []
        heapq.heappush(hq, [grid[0][0], 0, 0])
        maxFlow = 1
        while hq:
            current, x, y = heapq.heappop(hq)
            maxFlow = max(maxFlow, current)
            if x == n - 1 and y == n - 1:
                return maxFlow
            for nx, ny in [(x+1, y), (x-1,y), (x,y+1), (x,y-1)]:
                if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heapq.heappush(hq, [grid[nx][ny], nx, ny])


if __name__ == '__main__':
    sol = Solution()
    assert sol.swimInWater([[3,2],[0,1]]) == 3
    assert sol.swimInWater([[0,2],[1,3]]) == 3
    assert sol.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]) == 16
