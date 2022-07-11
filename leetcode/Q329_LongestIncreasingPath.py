from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(matrix: List[List[int]], x: int, y: int, dp: List[List[int]]) -> int:
            if dp[x][y] > 1:
                return dp[x][y]
            longestPath = 1
            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[x][y] < matrix[nx][ny]:
                    curPath = 1 + dfs(matrix, nx, ny, dp)
                    longestPath = max(longestPath, curPath)
            dp[x][y] = longestPath
            return longestPath

        dp = [[1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        longest = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(matrix, i, j, dp)
                longest = max(longest, dp[i][j])
        return longest


if __name__ == '__main__':
    sol = Solution()
    # assert sol.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4
    # assert sol.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4
    # assert sol.longestIncreasingPath([[7, 8, 9], [9, 7, 6], [7, 2, 3]]) == 6
    assert sol.longestIncreasingPath([[1, 2]]) == 2
