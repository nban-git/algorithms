from collections import defaultdict
from typing import List


class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        if len(segments) == 1:
            return segments
        segments.sort(key=lambda x: x[0])
        colors = defaultdict(int)
        for x, y, color in segments:
            colors[x] += color
            colors[y] -= color
        indices = sorted(colors.keys())
        result = []
        colorSum = 0
        for i in range(len(indices) - 1):
            colorSum += colors[indices[i]]
            if colorSum == 0: continue
            result.append([indices[i], indices[i + 1], colorSum])
        return result


if __name__ == '__main__':
    sol = Solution()
    # assert sol.splitPainting([[1, 4, 5], [4, 7, 7], [1, 7, 9]]) == [[1, 4, 14], [4, 7, 16]]
    # assert sol.splitPainting([[1, 7, 9], [6, 8, 15], [8, 10, 7]]) == [[1, 6, 9], [6, 7, 24], [7, 8, 15], [8, 10, 7]]
    assert sol.splitPainting([[1, 4, 5], [1, 4, 7], [4, 7, 1], [4, 7, 11]]) == [[1, 4, 12], [4, 7, 12]]
    assert sol.splitPainting([[4,16,12],[9,10,15],[18,19,13],[3,13,20],[12,16,3],[2,10,10],[3,11,4],[13,16,6]]) == [[2,3,10],[3,4,34],[4,9,46],[9,10,61],[10,11,36],[11,12,32],[12,13,35],[13,16,21],[18,19,13]]
    """
    1 +5 + 7
    4 - 5 - 7 + 1 + 11
    7 -1 - 11
    """