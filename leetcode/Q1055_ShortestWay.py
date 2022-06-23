class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        last = -1
        count = 0
        for i in range(len(target)):
            pos = -1
            for j in range(len(source)):
                if target[i] == source[j]:
                    pos = j
                    break
            if pos == -1:
                return -1
            if pos < last:
                count += 1
            else:
                if i == len(target) - 1 and pos > last:
                    count += 1
            last = pos
        print("source={}, target={}, count={}".format(source, target, count))
        return count


if __name__ == '__main__':
    sol = Solution()
    assert sol.shortestWay("abc", "abcbc") == 2
    assert sol.shortestWay("abc", "acdbc") == -1
    assert sol.shortestWay("xyz", "xzyxz") == 3
    assert sol.shortestWay("xzyx", "xzyxz") == 2
