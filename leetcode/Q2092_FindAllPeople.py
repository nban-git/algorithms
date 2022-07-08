from collections import defaultdict, deque
from itertools import groupby
from typing import List


class UF:
    def __init__(self, n: int):
        self.parent = list(range(n))
        # initializing rank with 0 causes TLE
        self.rank = [1] * n

    def find(self, p: int) -> int:
        while p != self.parent[p]:
            p = self.parent[p]
        return self.parent[p]

    def union(self, p: int, q: int):
        pp, qp = self.find(p), self.find(q)
        if pp == qp: return
        if self.rank[pp] > self.rank[qp]:
            qp, pp = pp, qp
        self.parent[pp] = qp
        self.rank[qp] += self.rank[pp]
        # The following causes TLE
        # if self.rank[pp] > self.rank[qp]:
        #     self.parent[qp] = pp
        #     self.rank[qp] += 1
        # else:
        #     self.parent[pp] = qp
        #     self.rank[pp] += 1

    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

    def reset(self, p: int):
        self.parent[p] = p


class Solution:
    # 2 <= n <= 10**5
    # 1 <= meetings.length <= 10**5
    def findAllPeople(self, n: int, meetings: List[List[int]], first: int) -> List[int]:
        uf = UF(n)
        uf.union(0, first)

        groups = defaultdict(list)
        for x, y, t in meetings:
            groups[t].append((x,y))
        groups = sorted(groups.items())

        # for _, group in groupby(sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2]):
        for _, group in groups:
            seen = set()
            for x, y in group:
                seen.add(x)
                seen.add(y)
                uf.union(x, y)
            for i in list(seen):
                if not uf.connected(i, 0):
                    uf.reset(i)

        result = []
        for i in range(n):
            if uf.connected(i, 0):
                result.append(i)
        return result


if __name__ == '__main__':
    sol = Solution()
    assert sol.findAllPeople(7, [[0, 1, 1], [1, 2, 1], [3, 4, 1], [1, 5, 1], [1, 5, 2], [2, 6, 2]], 1) == [0, 1, 2, 5, 6]
    assert sol.findAllPeople(6, [[1, 2, 5], [2, 3, 8], [1, 5, 10]], 1) == [0, 1, 2, 3, 5]
    assert sol.findAllPeople(4, [[3, 1, 3], [1, 2, 2], [0, 3, 3]], 3) == [0, 1, 3]
    assert sol.findAllPeople(5, [[3, 4, 2], [1, 2, 1], [2, 3, 1]], 1) == [0, 1, 2, 3, 4]
    assert sol.findAllPeople(5, [[1,4,3],[0,4,3]], 3) == [0, 1, 3, 4]
