from typing import List


class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        """
        odd jump    arr[i] <= arr[j]  arr[j] is the smallest
        even jump   arr[i] >= arr[j]  arr[j] is the smallest
        :param arr:
        :return:
        """
        return 0


if __name__ == '__main__':
    sol = Solution()
    assert sol.oddEvenJumps([10, 13, 12, 14, 15]) == 2
    assert sol.oddEvenJumps([2, 3, 1, 1, 4]) == 3
    assert sol.oddEvenJumps([5, 1, 3, 4, 2]) == 3
