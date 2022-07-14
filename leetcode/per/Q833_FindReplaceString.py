from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        for start, source, target in sorted(zip(indices, sources, targets), key=lambda i: i[0], reverse=True):
            end = start + len(source)
            if s[start:end] == source:
                s = s[:start] + target + s[end:]
        return s


if __name__ == '__main__':
    sol = Solution()
    assert sol.findReplaceString("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"]) == "eeebffff"
    assert sol.findReplaceString("abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"]) == "eeecd"
    assert sol.findReplaceString("abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"]) == "eeecd"
    assert sol.findReplaceString("vmokgggqzp", [3,5,1], ["kg","ggq","mo"], ["s","so","bfr"]) == "vbfrssozp"
    assert sol.findReplaceString("abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"]) == "eeecd"
    assert sol.findReplaceString("abcde", [2, 2], ["cdef", "bc"], ["f", "fe"]) == "abcde"
