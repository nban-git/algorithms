from typing import List


class TrieNode:
    def __init__(self, ch: str):
        self.path = {}
        self.isWord = False

    def insert(self, word: str):
        node = self
        for ch in word:
            if ch in node.path:
                node = node.path[ch]
            else:
                node.path[ch] = TrieNode(ch)
                node = node.path[ch]
        node.isWord = True

    def dicLenth(self, word):
        node = self
        for ch in word:
            if ch in node.path and node.path[ch].isWord:
                node = node.path[ch]
            else:
                return 0
        return len(word)


class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode("")
        for word in words:
            root.insert(word)

        longest = 0
        longestWord = ""
        for word in words:
            curLength = root.dicLenth(word)
            if curLength > longest or (curLength == longest and word < longestWord):
                longest = curLength
                longestWord = word
        return longestWord


if __name__ == '__main__':
    sol = Solution()
    assert sol.longestWord(["a","apple","banana","app","appl","ap","apply"]) == "apple"
    assert sol.longestWord(["w","wo","wor","worl","world"]) == "world"
    assert sol.longestWord(["wo","wor","worl","world"]) == ""
