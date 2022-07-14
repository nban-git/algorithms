from collections import defaultdict
from typing import List


class DetectSquares:

    def __init__(self):
        self.px = dict(set())
        self.py = dict(set())
        self.pmap = dict()

    def add(self, point: List[int]) -> None:
        x, y = point
        occur = self.pmap.get(point, 0)
        if point not in self.pmap.keys():
            self.px[x].add(y)
            self.py[y].add(x)
        self.pmap[point] = occur + 1

    def count(self, point: List[int]) -> int:
        cx, cy = point
        if cx not in self.px.keys() or cy not in self.py.keys():
            return 0
        self.pmap[point] = self.pmap[point] + 1
        count = 0
        for y in list(self.px[cx]):
            for x in list(self.py[y]):
                if [cx,cy] in self.pmap.keys() and [cx, y] in self.pmap.keys() \
                        and [x,cy] in self.pmap.keys() and [x, y] in self.pmap.keys():
                    count += max(max(self.pmap[[cx, cy]], self.pmap[[cx, cy]]),
                                 max(self.pmap[[cx, cy]], self.pmap[[cx, cy]]))
        return count


if __name__ == '__main__':
    detectSquares = DetectSquares()
    detectSquares.add([3, 10])
    detectSquares.add([11, 2])
    detectSquares.add([3, 2])
    print(detectSquares.count([11, 10]))

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
from collections import defaultdict
from typing import List


class DetectSquares:

    def __init__(self):
        self.px = dict(set())
        self.py = dict(set())
        self.pmap = dict()

    def add(self, point: List[int]) -> None:
        x, y = point
        occur = self.pmap.get(point, 0)
        if point not in self.pmap.keys():
            self.px[x].add(y)
            self.py[y].add(x)
        self.pmap[point] = occur + 1

    def count(self, point: List[int]) -> int:
        cx, cy = point
        if cx not in self.px.keys() or cy not in self.py.keys():
            return 0
        self.pmap[point] = self.pmap[point] + 1
        count = 0
        for y in list(self.px[cx]):
            for x in list(self.py[y]):
                if [cx,cy] in self.pmap.keys() and [cx, y] in self.pmap.keys() \
                        and [x,cy] in self.pmap.keys() and [x, y] in self.pmap.keys():
                    count += max(max(self.pmap[[cx, cy]], self.pmap[[cx, cy]]),
                                 max(self.pmap[[cx, cy]], self.pmap[[cx, cy]]))
        return count


if __name__ == '__main__':
    detectSquares = DetectSquares()
    detectSquares.add([3, 10])
    detectSquares.add([11, 2])
    detectSquares.add([3, 2])
    print(detectSquares.count([11, 10]))

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)