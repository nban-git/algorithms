from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 0 <= nums.length <= 105
        # -109 <= nums[i] <= 109
        # You must write an algorithm that runs in O(n) time.
        map = {}
        longest = 0
        for num in nums:
            if num not in map:
                left = map.get(num - 1, 0)
                right = map.get(num + 1, 0)
                length = right + left + 1
                map[num] = length
                longest = max(longest, length)

                map[num - left] = length
                map[num + right] = length
        return longest


def Q128():
    # HashTable UnionFind
    sol = Solution()
    assert sol.longestConsecutive([100,4,200,1,3,2]) == 4
    assert sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9


if __name__ == '__main__':
    Q128()
