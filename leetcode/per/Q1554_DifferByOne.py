from typing import List


class Solution:
    # This causes a memory exceed exception
    def differByOne2(self, dict: List[str]) -> bool:
        seen = set()
        for i in range(len(dict)):
            for j in range(len(dict[0])):
                key = dict[i][:j] + "." + dict[i][j+1:]
                if key in seen:
                    return True
                seen.add(key)
        return False

    def differByOne(self, dict: List[str]) -> bool:
        n, m = len(dict), len(dict[0])
        DIST = 10 ** 11 + 7
        hashes = [0] * n
        for i in range(n):
            for j in range(m):
                hashes[i] = (26 * hashes[i] + (ord(dict[i][j]) - ord('a'))) % DIST

        base = 1
        for j in range(m-1,-1,-1):
            # going reverse because base goes from right to left
            seen = set()
            for i in range(n):
                key = (hashes[i] - (ord(dict[i][j]) - ord('a')) * base) % DIST
                if key in seen:
                    return True
                seen.add(key)
            base = 26 * base % DIST
        return False
        # n, m = len(dict), len(dict[0])
        # hashes = [0] * n
        # MOD = 10 ** 11 + 7
        #
        # for i in range(n):
        #     for j in range(m):
        #         hashes[i] = (26 * hashes[i] + (ord(dict[i][j]) - ord('a'))) % MOD
        #
        # base = 1
        # for j in range(m - 1, -1, -1):
        #     seen = set()
        #     for i in range(n):
        #         new_h = (hashes[i] - base * (ord(dict[i][j]) - ord('a'))) % MOD
        #         if new_h in seen:
        #             return True
        #         seen.add(new_h)
        #     base = 26 * base % MOD
        # return False

if __name__ == '__main__':
    sol = Solution()
    assert sol.differByOne(["abcd","acbd", "aacd"])
    assert not sol.differByOne(["ab","cd","yz"])
    assert sol.differByOne(["abcd","cccc","abyd","abab"])
    assert sol.differByOne(["abc","dfe","abf"])
    assert not sol.differByOne(["abcde","abaaa","aaade"])
