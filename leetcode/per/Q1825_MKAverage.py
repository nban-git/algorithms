import heapq


class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.sum = 0
        self.idx = 0
        self.divider = m - 2 * k
        self.container = []
        self.minq = []
        self.maxq = []

    def addElement(self, num: int) -> None:
        self.container.append(num)
        self.sum += num
        heapq.heappush(self.minq, (num, self.idx))
        heapq.heappush(self.maxq, (-num, self.idx))
        self.idx += 1
        if self.idx > self.m:
            passed = self.container[self.idx - self.m - 1]
            self.sum -= passed

    def calculateMKAverage(self) -> int:
        print(self.minq)
        print(self.maxq)
        if self.idx < self.m:
            return -1
        tempSum = self.sum
        tempContainer = []
        count = 0
        while count < self.k:
            small, id = heapq.heappop(self.minq)
            if id >= self.idx - self.m:
                tempSum -= small
                count += 1
                tempContainer.append((small,id))
        for t in tempContainer:
            heapq.heappush(self.minq, t)
        print(self.minq)

        tempContainer = []
        count = 0
        while count < self.k:
            large, id = heapq.heappop(self.maxq)
            if id >= self.idx - self.m:
                tempSum += large
                count += 1
                tempContainer.append((large, id))
        for t in tempContainer:
            heapq.heappush(self.maxq, t)

        return tempSum // self.divider


if __name__ == '__main__':
    obj = MKAverage(3, 1)
    obj.addElement(3)
    obj.addElement(1)
    print(obj.calculateMKAverage())
    obj.addElement(10)
    print(obj.calculateMKAverage())
    obj.addElement(5)
    obj.addElement(5)
    obj.addElement(5)
    print(obj.calculateMKAverage())