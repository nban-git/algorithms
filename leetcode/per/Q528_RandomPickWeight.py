from typing import List
import random


class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        for i in range(1, len(w)):
            self.w[i] += self.w[i - 1]

    def pickIndex(self) -> int:
        index = random.randint(1, self.w[-1])
        # index = 4
        l, r = 0, len(self.w) - 1
        while l < r:
            m = (l + r) // 2
            if index <= self.w[m]:
                r = m
            else:
                l = m + 1
        return l


if __name__ == '__main__':
    sol = Solution([1, 3, 4])
    print(sol.pickIndex())
    print(sol.pickIndex())
    print(sol.pickIndex())
    print(sol.pickIndex())
    print(sol.pickIndex())
    print(sol.pickIndex())
    print(sol.pickIndex())
    print(sol.pickIndex())
    print(sol.pickIndex())
    print(sol.pickIndex())
    print(sol.pickIndex())


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()