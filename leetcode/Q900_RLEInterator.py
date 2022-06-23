import bisect
from typing import List


class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.indices = [encoding[0]]
        self.values = [encoding[1]]
        self.iter = 0
        self.cur = 0
        for i in range(2, len(encoding), 2):
            if encoding[i] == 0: continue
            self.indices.append(self.indices[-1] + encoding[i])
            self.values.append(encoding[i+1])

    def next(self, n: int) -> int:
        self.cur += n
        idx = bisect.bisect_left(self.indices, self.cur)
        return self.values[idx] if idx < len(self.indices) else -1

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)


if __name__ == '__main__':
    rle = RLEIterator([3, 8, 0, 9, 2, 5])
    assert rle.next(2) == 8
    assert rle.next(1) == 8
    assert rle.next(1) == 5
    assert rle.next(2) == -1

    rle = RLEIterator([784,303,477,583,909,505])
    print(rle.next(130))
    print(rle.next(333))
    print(rle.next(238))
    print(rle.next(87))
    print(rle.next(301))
    print(rle.next(276))
