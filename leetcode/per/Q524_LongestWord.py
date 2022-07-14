from collections import defaultdict
from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))
        for word in dictionary:
            i = 0
            for ch in s:
                if word[i] == ch:
                    i += 1
                    if i == len(word):
                        return word
        return ""


if __name__ == '__main__':
    sol = Solution()
    assert sol.findLongestWord(s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]) == "apple"
    assert sol.findLongestWord(s = "abpcplea", dictionary = ["a","b","c"]) == "a"
    assert sol.findLongestWord("abce", ["abe","abc"]) == "abc"
    assert sol.findLongestWord("aaa", ["aaa","aa","a"]) == "aaa"

