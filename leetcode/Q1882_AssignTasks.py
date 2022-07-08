import heapq
from collections import defaultdict
from typing import List


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        result = []
        workers = []
        for i, s in enumerate(servers):
            heapq.heappush(workers, (s, i, 0))

        assigned = []
        for i, task in enumerate(tasks):
            while assigned and assigned[0][0] <= i or not workers:
                time, server, idx = heapq.heappop(assigned)
                heapq.heappush(workers, (server, idx, time))
            server, idx, time = heapq.heappop(workers)
            heapq.heappush(assigned, (max(time,i) + task, server, idx))
            result.append(idx)
        return result


if __name__ == '__main__':
    sol = Solution()
    assert sol.assignTasks(servers = [3,3,2], tasks = [1,2,3,2,1,2]) == [2,2,0,2,1,2]
    assert sol.assignTasks(servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]) == [1,4,1,4,1,3,2]
    assert sol.assignTasks(servers=[10,63,95,16,85,57,83,95,6,29,71], tasks=[70,31,83,15,32,67,98,65,56,48,38,90,5]) == [8,0,3,9,5,1,10,6,4,2,7,9,0]
