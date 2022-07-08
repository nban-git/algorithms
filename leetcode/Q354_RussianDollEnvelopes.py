import bisect
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        seq = []
        for e in envelopes:
            if not seq or seq[-1] < e[1]:
                seq.append(e[1])
            else:
                idx = bisect.bisect_left(seq, e[1])
                seq[idx] = e[1]
        return len(seq)


if __name__ == '__main__':
    sol = Solution()
    assert sol.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]) == 3
    assert sol.maxEnvelopes([[1,1],[1,1],[1,1]]) == 1
    assert sol.maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1]]) == 4
    assert sol.maxEnvelopes([[46,89],[50,53],[52,68],[72,45],[77,81]]) == 3
