from collections import defaultdict
from typing import List


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        startWordSet = set()
        for s in startWords:
            startWordSet.add("".join(sorted(s)))

        count = 0
        for t in targetWords:
            word = "".join(sorted(t))
            for i in range(len(word)):
                if (word[:i] + word[i+1:]) in startWordSet:
                    count += 1
                    break
        return count


if __name__ == '__main__':
    sol = Solution()
    assert sol.wordCount(["ab","a"], ["abc","abcd"]) == 1
    assert sol.wordCount(["ant","act","tack"], ["tack","act","acti"]) == 2
    assert sol.wordCount(["lhum", "bim", "cyjhm", "h", "a", "ljxd", "run", "zrl", "dmf", "y"],
                         ["da", "lzkr", "uzc", "jdxlz", "yt", "emdf"]) == 5
    assert sol.wordCount(["g","vf","ylpuk","nyf","gdj","j","fyqzg","sizec"],
                         ["r","am","jg","umhjo","fov","lujy","b","uz","y"]) == 2