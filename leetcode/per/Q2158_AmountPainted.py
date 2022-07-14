from typing import List


class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        result = []
        return result


if __name__ == '__main__':
    sol = Solution()
    assert sol.amountPainted([[1, 4], [4, 7], [5, 8]]) == [3, 3, 1]
    assert sol.amountPainted([[0, 5], [0, 2], [0, 3], [0, 4], [0, 5]]) == [5, 0, 0, 0, 0]
    assert sol.amountPainted([[3, 5], [1, 3], [4, 5], [3, 4]]) == [2, 2, 0, 0]
    assert sol.amountPainted([[1, 5], [2, 4]]) == [4, 0]
    assert sol.amountPainted([[1, 4], [5, 8], [4, 7]]) == [3, 3, 1]
    assert sol.amountPainted([[2, 4], [0, 4], [1, 4], [1, 5], [0, 2]]) == [2, 2, 0, 1, 0]
    assert sol.amountPainted([[4, 5], [18, 19], [9, 11], [8, 13], [14, 19], [17, 19], [6, 19], [19, 20]]) == [1, 1, 2,
                                                                                                              3, 4, 0,
                                                                                                              3, 1]
