from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        for i in range(n):
            if citations[i] >= n - i:
                return n - i
        return 0


if __name__ == '__main__':
    sol = Solution()
    assert sol.hIndex([2,0,6,3,5,1,4,7,8,9]) == 5
    assert sol.hIndex([3,0,6,1,5]) == 3
    assert sol.hIndex([1,3,1]) == 1
