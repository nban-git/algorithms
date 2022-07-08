from collections import defaultdict
from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = defaultdict(int)

        def find(x: int):
            if x != parent[x]:
                parent[x] = parent[x]
            return parent[x]

        def union(x: int, y: int):
            parent.setdefault(x, x)
            parent.setdefault(y, y)
            xp = find(x)
            yp = find(y)
            parent[xp] = yp

        for x, y in stones:
            union(x, ~y)

        print({find(x) for x in parent})

        return len(stones) - len({find(x) for x in parent})


if __name__ == '__main__':
    sol = Solution()
    assert sol.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]) == 5
    # assert sol.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]) == 3
    # assert sol.removeStones([[0,0]]) == 0
