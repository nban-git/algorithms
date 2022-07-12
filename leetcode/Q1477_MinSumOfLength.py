import heapq
from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        start, curSum = 0, 0
        hq = []
        for i in range(len(arr)):
            curSum += arr[i]
            while curSum > target:
                curSum -= arr[start]
                start += 1
            if curSum == target:
                heapq.heappush(hq, i - start + 1)
                curSum -= arr[start]
                start += 1

        if len(hq) < 2:
            return -1
        return heapq.heappop(hq) + heapq.heappop(hq)


if __name__ == '__main__':
    sol = Solution()
    assert sol.minSumOfLengths([3,2,2,4,3], 3) == 2
    assert sol.minSumOfLengths([7,3,4,7], 7) == 2
    assert sol.minSumOfLengths([4,3,2,6,2,3,4], 6) == -1
    assert sol.minSumOfLengths([1,2,2,3,2,6,7,2,1,4,8], 5) == 4  # -3 -2 -2