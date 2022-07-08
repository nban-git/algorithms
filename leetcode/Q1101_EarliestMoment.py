from collections import defaultdict
from typing import List


class UF:
    def __init__(self, n: int):
        self.friend = defaultdict(int)
        self.rank = defaultdict(int)
        self.groups = n

    def find(self, x):
        while x != self.friend[x]:
            x = self.friend[x]
        return x


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        friend = [i for i in range(n)]
        groups = n

        for t, x, y in logs:
            union(x, y)
            if groups == -1:
                return t
        return -1
