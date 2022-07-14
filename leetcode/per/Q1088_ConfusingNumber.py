import bisect


class Solution:
    def confusingNumberII(self, n: int) -> int:
        ones = [6, 9]
        first = [1, 6, 8, 9]
        tens = {
            0: [1, 6, 8, 9],
            1: [0, 6, 8, 9],
            6: [0, 1, 6, 8],
            8: [0, 1, 6, 9],
            9: [0, 1, 8, 9]
        }

        if n <= 10:
            idx = bisect.bisect_right(ones, n)
            print(idx)
            return idx

        if n <= 100:
            idx = bisect.bisect_right(first, n / 100)


        return 0


if __name__ == '__main__':
    sol = Solution()
    sol.confusingNumberII(5)
    sol.confusingNumberII(6)
    sol.confusingNumberII(8)
    sol.confusingNumberII(9)
    sol.confusingNumberII(10)