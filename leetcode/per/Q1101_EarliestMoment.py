from collections import defaultdict
from typing import List


class UF:
    def __init__(self, n: int):
        self.friend = [i for i in range(n)]
        self.rank = [1] * n
        self.groups = n

    def find(self, x):
        while x != self.friend[x]:
            x = self.friend[x]
        return x

    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return

        if self.rank[fx] > self.rank[fy]:
            self.friend[fx] = fy
            self.rank[fy] += 1
        else:
            self.friend[fy] = fx
            self.rank[fx] += 1
        self.groups -= 1


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda x: x[0])
        uf = UF(n)
        for t, x, y in logs:
            uf.union(x, y)
            if uf.groups == 1:
                return t
        return -1


if __name__ == '__main__':
    sol = Solution()
    assert sol.earliestAcq([[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], 6) == 20190301
    assert sol.earliestAcq([[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], 4) == 3
