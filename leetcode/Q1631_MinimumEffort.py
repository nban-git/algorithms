import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        r, c = len(heights), len(heights[0])
        paths = [[float("inf") for _ in range(c)] for _ in range(r)]
        paths[0][0] = 0

        hq = []
        heapq.heappush(hq, (0, 0, 0))
        while hq:
            diff, x, y = heapq.heappop(hq)
            if diff > paths[x][y]: continue
            if x == r-1 and y == c-1: return paths[x][y]
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c:
                    ndiff = max(diff, abs(heights[nx][ny] - heights[x][y]))
                    if paths[nx][ny] > ndiff:
                        paths[nx][ny] = ndiff
                        heapq.heappush(hq, (ndiff, nx, ny))


if __name__ == '__main__':
    sol = Solution()
    assert sol.minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]) == 2
    assert sol.minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]) == 1
    assert sol.minimumEffortPath(
        [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]) == 0
    assert sol.minimumEffortPath([[1, 10, 6, 7, 9, 10, 4, 9]]) == 9
