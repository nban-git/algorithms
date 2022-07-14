import bisect
from typing import List

# Check how to print the path
# https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326308/C%2B%2BPython-DP-Binary-Search-BIT-Solutions-Picture-explain-O(NlogN)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = []
        for num in nums:
            if len(seq) == 0 or seq[-1] < num:
                seq.append(num)
            else:
                idx = bisect.bisect_left(seq, num)
                seq[idx] = num
        return len(seq)


if __name__ == '__main__':
    sol = Solution()
    assert sol.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
    assert sol.lengthOfLIS([0,1,0,3,2,3]) == 4
    assert sol.lengthOfLIS([7,7,7,7,7,7,7]) == 1