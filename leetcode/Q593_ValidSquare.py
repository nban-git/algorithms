from collections import defaultdict
from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(p1: List[int], p2: List[int]):
            return (p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2

        d = []
        points = [p1, p2, p3, p4]
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                d.append(distance(points[i], points[j]))
        d.sort()
        return d[0] == d[1] == d[2] == d[3] and d[4] == 2 * d[0] and d[4] == d[5]


if __name__ == '__main__':
    sol = Solution()
    assert sol.validSquare(p1=[0, 0], p2=[1, 1], p3=[1, 0], p4=[0, 1])
    assert not sol.validSquare(p1=[0, 0], p2=[1, 1], p3=[1, 0], p4=[0, 12])
    assert sol.validSquare(p1=[1, 0], p2=[-1, 0], p3=[0, 1], p4=[0, -1])
    assert not sol.validSquare([0, 0], [0, 0], [0, 0], [0, 0])
