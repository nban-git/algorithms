from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        count = 0
        curMax = 0
        for a, d in properties:
            if d < curMax:
                count += 1
            else:
                curMax = d
        return count


if __name__ == '__main__':
    sol = Solution()
    assert sol.numberOfWeakCharacters([[5,5],[6,3],[3,6]]) == 0
    assert sol.numberOfWeakCharacters([[2,2],[3,3]]) == 1
    assert sol.numberOfWeakCharacters([[1,5],[10,4],[4,3]]) == 1
    assert sol.numberOfWeakCharacters([[1,5],[10,5],[4,3],[6,4]]) == 2
    assert sol.numberOfWeakCharacters([[1,1],[2,1],[2,2],[1,2]]) == 1
