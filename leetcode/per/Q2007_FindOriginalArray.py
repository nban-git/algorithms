import collections
from collections import defaultdict
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        c = collections.Counter(changed)
        original = []
        for i in sorted(changed):
            if c[i] > 0:
                if c[i * 2] == 0:
                    return []
                c[i] -= 1
                c[i * 2] -= 1
                if c[i * 2] < 0: return []
                original.append(i)
        return original

if __name__ == '__main__':
    sol = Solution()
    assert sol.findOriginalArray([0,0,0,0]) == [0,0]
    assert sol.findOriginalArray([1,3,4,2,6,8]) == [1,3,4]
    assert sol.findOriginalArray([6,3,0,1]) == []
    assert sol.findOriginalArray([1]) == []


