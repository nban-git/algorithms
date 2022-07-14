import bisect


class RangeModule:

    def __init__(self):
        self.range = list()

    def addRange(self, left: int, right: int) -> None:
        if len(self.range) == 0:
            self.range.append([left, right])
        else:
            l = bisect.bisect_left(self.range, left, key=lambda i: i[0])
            r = bisect.bisect_left(self.range, right, key=lambda i: i[0])
            del self.range[l:r-1]
            self.range.insert(l, min(self.range[l], left), max(self.range[r], right))

    def queryRange(self, left: int, right: int) -> bool:
        l = bisect.bisect_left(self.range, left, key=lambda i: i[0])
        r = bisect.bisect_left(self.range, right, key=lambda i: i[0])
        return l == r

    def removeRange(self, left: int, right: int) -> None:
        l = bisect.bisect_left(self.range, left, key=lambda i: i[0])
        r = bisect.bisect_left(self.range, right, key=lambda i: i[0])



# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)


if __name__ == '__main__':
    range = [[10,15]]
    print(bisect.bisect(range, 9, key=lambda i: i[0]))
    print(bisect.bisect(range, 15, key=lambda i: i[1]))
    l = bisect.bisect(range, 9, key=lambda i: i[0])
    r = bisect.bisect(range, 12, key=lambda i: i[0])
    # if l > len(range):
    new_range = [min(range[l][0], 9), max(range[r-1][1], 12)]
    del range[l:r]
    range.insert(l, new_range)

    # l = bisect.bisect(range, 15, key=lambda i: i[0])
    # r = bisect.bisect(range, 20, key=lambda i: i[0])
    # new_range = [min(range[l][0], 15), max(range[r-1][1], 20)]
    # del range[l:r]
    # range.insert(l, new_range)
    #
    # print(bisect.bisect(range, 30, key=lambda i: i[0]))
    # print(bisect.bisect_left(range, 9, key=lambda i: i[0]))
    # print(bisect.bisect_left(range, 11, key=lambda i: i[0]))
    # print(bisect.bisect_left(range, 30, key=lambda i: i[0]))
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
