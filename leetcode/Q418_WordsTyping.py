from typing import List


class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = " ".join(sentence) + " "
        start, slen = 0, len(s)
        for i in range(rows):
            start += cols
            if s[start % slen] == ' ':
                start += 1
            else:
                while start > 0 and s[(start-1) % slen] != ' ':
                    start -= 1
        return start // slen


if __name__ == '__main__':
    sol = Solution()
    assert sol.wordsTyping(sentence=["hello", "world"], rows=2, cols=8) == 1
    assert sol.wordsTyping(sentence=["a", "bcd", "e"], rows=3, cols=6) == 2
    assert sol.wordsTyping(sentence=["i", "had", "apple", "pie"], rows=4, cols=5) == 1
    assert sol.wordsTyping(sentence=["a"], rows=10000, cols=10000) == 50000000
