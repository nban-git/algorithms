import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        candidates = sorted([(task[0], task[1], i) for i, task in enumerate(tasks)])

        result = []
        runners = []
        last = 0
        for start, duration, idx in candidates:
            while runners and start > last:
                # Order matters. Later, the one pushed first will be handled first
                d, i, s = heapq.heappop(runners)
                last = max(s, last) + d
                result.append(i)
            heapq.heappush(runners, (duration, idx, start))
        while runners:
            result.append(heapq.heappop(runners)[1])
        return result


if __name__ == '__main__':
    sol = Solution()
    assert sol.getOrder([[1,2],[2,4],[3,2],[4,1]]) == [0,2,3,1]
    assert sol.getOrder([[1,3],[3,4],[3,2],[4,1]]) == [0,3,2,1]
    assert sol.getOrder([[7,10],[7,12],[7,5],[7,4],[7,2]]) == [4,3,2,0,1]
    assert sol.getOrder([[6,10],[7,12],[7,5],[7,4],[8,2]]) == [0,4,3,2,1]
    assert sol.getOrder([[1,10],[7,12],[7,5],[7,4],[13,2]]) == [0,3,4,2,1]
    assert sol.getOrder([[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]) == [6,1,2,9,4,10,0,11,5,13,3,8,12,7]
