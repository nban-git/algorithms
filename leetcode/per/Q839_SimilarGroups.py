from collections import deque
from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i+1, n):
                if sum(strs[i][k] != strs[j][k] for k in range(len(strs[i]))) in (0,2):
                    uf.union(i, j)
        return len(set([uf.find(i) for i in range(n)]))


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, p: str) -> str:
        while self.parent[p] != p:
            p = self.parent[p]
        return p

    def union(self, p: str, q: str):
        pp = self.find(p)
        qp = self.find(q)
        if pp == qp:
            return
        if self.rank[pp] > self.rank[qp]:
            self.parent[qp] = pp
        else:
            self.parent[pp] = qp
        if self.parent[pp] == self.parent[qp]:
            self.rank[qp] += 1


if __name__ == '__main__':
    sol = Solution()
    assert sol.numSimilarGroups(["tars","rats","arts","star"]) == 2
    assert sol.numSimilarGroups(["omv","ovm"]) == 1
