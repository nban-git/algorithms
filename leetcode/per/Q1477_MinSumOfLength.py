import heapq
from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        start, curSum = 0, 0
        dp = [float("inf")] * len(arr)
        bestsofar, minSum = float("inf"), float("inf")
        for i in range(len(arr)):
            curSum += arr[i]
            while curSum > target:
                curSum -= arr[start]
                start += 1
            if curSum == target:
                if start > 0 and dp[start-1] != float("inf"):
                    minSum = min(minSum, dp[start-1] + (i-start+1))
                bestsofar = min(bestsofar, i-start+1)
            dp[i] = bestsofar

        return -1 if minSum == float("inf") else minSum


if __name__ == '__main__':
    sol = Solution()
    assert sol.minSumOfLengths([3,2,2,4,3], 3) == 2
    assert sol.minSumOfLengths([7,3,4,7], 7) == 2
    assert sol.minSumOfLengths([4,3,2,6,2,3,4], 6) == -1
    assert sol.minSumOfLengths([1,2,2,3,2,6,7,2,1,4,8], 5) == 4
    assert sol.minSumOfLengths([1,6,1], 7) == -1
    assert sol.minSumOfLengths([2,1,3,3,2,3,1], 6) == 5
