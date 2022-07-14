class Solution:
    # https://leetcode.com/problems/shortest-way-to-form-string/discuss/330938/Accept-is-not-enough-to-get-a-hire.-Interviewee-4-follow-up
    def shortestWay(self, source: str, target: str) -> int:
        count = 0
        t = 0
        while t < len(target):
            start = t
            s = 0
            while t < len(target) and s < len(source):
                if target[t] == source[s]:
                    t += 1
                    s += 1
                else:
                    s += 1
            if start == t:
                return -1
            count += 1
        return count


if __name__ == '__main__':
    sol = Solution()
    assert sol.shortestWay("abc", "abcbc") == 2
    assert sol.shortestWay("abc", "acdbc") == -1
    assert sol.shortestWay("xyz", "xzyxz") == 3
    assert sol.shortestWay("xzyx", "xzyxz") == 2
    assert sol.shortestWay("aaaaa", "aaaaaaaaaaaaa") == 3
