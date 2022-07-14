from typing import List


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        turn = 0
        rows, cols, diag = [0] * 3, [0] * 3, [0] * 2
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    turn += 1
                    rows[j] += 1
                    cols[i] += 1
                    if i == j:
                        diag[0] += 1
                    if i+j == 2:
                        diag[1] += 1
                elif board[i][j] == "O":
                    turn -= 1
                    rows[j] -= 1
                    cols[i] -= 1
                    if i == j:
                        diag[0] -= 1
                    if i+j == 2:
                        diag[1] -= 1
        xwin, owin = False, False
        for i in range(len(rows)):
            xwin = xwin or rows[i] == 3 or cols[i] == 3
            owin = owin or rows[i] == -3 or cols[i] == -3
        for i in range(len(diag)):
            xwin = xwin or diag[i] == 3
            owin = owin or diag[i] == -3

        if (xwin and turn == 0) or (owin and turn == 1):
            return False
        return (turn == 0 or turn == 1) and (not xwin or not owin)


if __name__ == '__main__':
    sol = Solution()
    assert not sol.validTicTacToe(["O  ","   ","   "])
    assert not sol.validTicTacToe(["XOX"," X ","   "])
    assert sol.validTicTacToe(["XOX","O O","XOX"])
    assert sol.validTicTacToe(["XO ","O O","X X"])
    assert sol.validTicTacToe(["XOX","XOO","OXX"])
    assert not sol.validTicTacToe(["XOX","XOO","OOX"])
    assert not sol.validTicTacToe(["XOX","XOX","XOX"])
    assert not sol.validTicTacToe(["XXO","XOX","OXO"])
    assert sol.validTicTacToe(["XXX","OOX","OOX"])