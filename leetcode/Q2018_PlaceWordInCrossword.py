from typing import List


class Solution:
    def placeWordInCrossword_NotWorking(self, board: List[List[str]], word: str) -> bool:
        def isValid(r: int, c: int) -> bool:
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] not in (" ", "#"):
                return False
            return True

        def isPlaced(r: int, c: int, word: str) -> bool:
            print("Starting from r={}, c={}".format(r, c))
            for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
                if not isValid(r-dx, c-dy):
                    continue
                nx, ny = r, c
                found = True
                for i in range(1, len(word)):
                    nx += dx
                    ny += dy
                    print("nx={}, ny={}, ch={}".format(nx, ny, word[i]))
                    if board[nx][ny] not in (" ", word[i]):
                        found = False
                        break
                if found and isValid(nx+dx, ny+dy):
                    return True
            return False

        print("Test={}".format(board))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != "#":
                    if isPlaced(i, j, word):
                        return True
        return False

    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        print(list(zip(*board)))
        words=[word,word[::-1]]
        n=len(word)
        for B in board,zip(*board):
            for row in B:
                q=''.join(row).split('#')
                for w in words:
                    for s in q:
                        if len(s)==n:
                            if all(s[i]==w[i] or s[i]==' ' for i in range(n)):
                                return True
        return False

if __name__ == '__main__':
    sol = Solution()
    assert sol.placeWordInCrossword([["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], "abc")
    assert sol.placeWordInCrossword([[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], "ac") == False
    assert sol.placeWordInCrossword([["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], "ca")
