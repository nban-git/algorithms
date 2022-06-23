from collections import defaultdict
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        dist = defaultdict(int)
        for trip in trips:
            dist[trip[1]] += trip[0]
            dist[trip[2]] -= trip[0]
        pos = sorted(dist.keys())
        maxRider, curRider = 0, 0
        for p in pos:
            curRider += dist[p]
            maxRider = max(maxRider, curRider)
        return maxRider <= capacity


if __name__ == '__main__':
    sol = Solution()
    assert sol.carPooling([[2,1,5],[3,3,7]], 4) == False
    assert sol.carPooling([[2,1,5],[3,3,7]], 5) == True
    assert sol.carPooling([[2,1,5],[3,3,7], [6,5,10]], 8) == False
    assert sol.carPooling([[2,1,5],[3,3,7], [6,5,10]], 9) == True
    assert sol.carPooling([[9, 3, 4], [9, 1, 7], [4, 2, 4], [7, 4, 5]], 23) == True

