import heapq
from typing import List


class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        hq = []
        heapq.heappush(hq, (-grid[0][0], grid[0][0], 0, 0))
        visited = set()
        while hq:
            value, minpath, x, y = heapq.heappop(hq)
            visited.add((x, y))
            if x == len(grid)-1 and y == len(grid[0])-1:
                return minpath
            for dx, dy in [[0,1], [0,-1], [1,0], [-1,0]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited:
                    minstore = grid[nx][ny] if minpath > grid[nx][ny] else minpath
                    heapq.heappush(hq, (-grid[nx][ny], minstore, nx, ny))


if __name__ == '__main__':
    sol = Solution()
    assert sol.maximumMinimumPath([[5,4,5],[1,2,6],[7,4,6]]) == 4
    assert sol.maximumMinimumPath([[2,2,1,2,2,2],[1,2,2,2,1,2]]) == 2
    assert sol.maximumMinimumPath([[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]) == 3
