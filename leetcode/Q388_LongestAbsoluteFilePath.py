class Solution:
    def lengthLongestPath(self, input: str) -> int:
        s, e, longest = 0, 0, 0
        stack = []
        lines = input.split("\n")
        for line in lines:
            level = line.count("\t")
            fpath = line[level:]

            while len(stack) > level:
                stack.pop()
            plength = stack[-1] if stack else 0

            if 0 < fpath.find('.') < len(fpath):
                longest = max(longest, plength + len(fpath))
            else:
                stack.append(plength + len(fpath) + 1)
        return longest


if __name__ == '__main__':
    sol = Solution()
    assert sol.lengthLongestPath("a\n\tb.txt\na2\n\tb2.txt") == 9
    assert sol.lengthLongestPath("file1.txt\nfile2.txt\nlongfile.txt") == 12
    assert sol.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2") == 21
    assert sol.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext") == 20
    assert sol.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext\n\tsubdir3") == 20
    assert sol.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
) == 32
    assert sol.lengthLongestPath("a") == 0
