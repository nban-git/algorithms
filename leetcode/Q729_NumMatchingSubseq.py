from collections import defaultdict
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dict = defaultdict(list)
        for word in words:
            dict[word[0]].append(word)

        count = 0
        for ch in s:
            matched = dict[ch]
            dict[ch] = []
            for mword in matched:
                if len(mword) == 1:
                    count += 1
                else:
                    dict[mword[1]].append(mword[1:])
        return count


if __name__ == '__main__':
    sol = Solution()
    assert sol.numMatchingSubseq("abcde", ["a","bb","acd","ace"]) == 3
    assert sol.numMatchingSubseq("dsahjpjauf", ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]) == 2
    # assert sol.numMatchingSubseq() == 3
