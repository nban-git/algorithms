from math import ceil
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result, line = [], []
        capacity = maxWidth
        for w in words:
            if capacity - len(w) - len(line) < 0:
                wcount = len(line) - 1
                for i in range(capacity):
                    if wcount == 0:
                        line[0] += ' '
                    else:
                        line[i % wcount] += ' '
                result.append(''.join(line))
                line = []
                capacity = maxWidth
            line.append(w)
            capacity = capacity - len(w)
        last = ' '.join(line)
        last += ' ' * (maxWidth - len(last))
        result.append(last)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
    print(sol.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
    print(sol.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))
