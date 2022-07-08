import bisect


class RangeModule:

    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.ranges, left)
        end = bisect.bisect_right(self.ranges, right)

        subrange = []
        if start % 2 == 0:
            subrange.append(left)
        if end % 2 == 0:
            subrange.append(right)
        self.ranges[start:end] = subrange

    def queryRange(self, left: int, right: int) -> bool:
        start = bisect.bisect_right(self.ranges, left)
        end = bisect.bisect_left(self.ranges, right)

        return start == end and start % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.ranges, left)
        end = bisect.bisect_right(self.ranges, right)

        subrange = []
        if start % 2 == 1:
            subrange.append(left)
        if end % 2 == 1:
            subrange.append(right)
        self.ranges[start:end] = subrange


if __name__ == '__main__':
    obj = RangeModule()
    obj.addRange(10, 20)
    obj.removeRange(14, 16)
    assert obj.queryRange(10, 14)
    assert not obj.queryRange(13, 15)
    assert obj.queryRange(16, 17)
