class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        def neighbors(i, j):
            return sum(board[r][c] & 1
                for r in range(i-1, i+2)
                for c in range(j-1, j+2)
                if (r,c) != (i,j) and 0<=r<m and 0<=c<n)
        for i in range(m):
            for j in range(n):
                live = neighbors(i, j)
                if board[i][j] == 1 and live in (2,3):
                    board[i][j] |= 2
                elif board[i][j] == 0 and live == 3:
                    board[i][j] |= 2
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1