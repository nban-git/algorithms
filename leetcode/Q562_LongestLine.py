from typing import List


class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        dp = [[[0] * 4 for _ in range(m)] for _ in range(n)]

        longest = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    continue
                for k in range(4):
                    dp[i][j][k] = 1
                if i > 0:  # vertical
                    dp[i][j][0] += dp[i-1][j][0]
                if j > 0:  # horizontal
                    dp[i][j][1] += dp[i][j-1][1]
                if i > 0 and j > 0:  # diagonal
                    dp[i][j][2] += dp[i - 1][j-1][2]
                if i > 0 and j < m-1:
                    dp[i][j][3] += dp[i - 1][j+1][3]
                longest = max(longest, dp[i][j][0], dp[i][j][1], dp[i][j][2], dp[i][j][3])
        return longest


if __name__ == '__main__':
    sol = Solution()
    assert sol.longestLine([[0,1,1,0],[0,1,1,0],[0,0,0,1]]) == 3
    assert sol.longestLine([[1,1,1,1],[0,1,1,0],[0,0,0,1]]) == 4
    assert sol.longestLine([[1,0,0,1],[0,1,1,0],[1,0,0,0]]) == 2
    assert sol.longestLine([[1,1,0,0,1,0,0,1,1,0],[1,0,0,1,0,1,1,1,1,1],[1,1,1,0,0,1,1,1,1,0],[0,1,1,1,0,1,1,1,1,1],[0,0,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,0,1,1,1],[0,1,1,1,1,1,1,0,0,1],[1,1,1,1,1,0,0,1,1,1],[0,1,0,1,1,0,1,1,1,1],[1,1,1,0,1,0,1,1,1,1]]) == 9

"""    
[1,1,0,0,1,0,0,1,1,0]
[1,0,0,1,0,1,1,1,1,1]
[1,1,1,0,0,1,1,1,1,0]
[0,1,1,1,0,1,1,1,1,1],
[0,0,1,1,1,1,1,1,1,0],
[1,1,1,1,1,1,0,1,1,1],
[0,1,1,1,1,1,1,0,0,1],
[1,1,1,1,1,0,0,1,1,1],
[0,1,0,1,1,0,1,1,1,1],
[1,1,1,0,1,0,1,1,1,1]]) == 8
"""