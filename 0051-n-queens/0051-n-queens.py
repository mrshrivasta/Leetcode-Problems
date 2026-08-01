class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols     = set()   # columns with a queen
        diag1    = set()   # (row - col) constant on \ diagonals
        diag2    = set()   # (row + col) constant on / diagonals

        result   = []
        queens   = []      # queens[row] = col placement

        def backtrack(row: int) -> None:
            if row == n:
                board = []
                for c in queens:
                    board.append('.' * c + 'Q' + '.' * (n - c - 1))
                result.append(board)
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # Place queen
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                queens.append(col)

                backtrack(row + 1)

                # Remove queen
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
                queens.pop()

        backtrack(0)
        return result