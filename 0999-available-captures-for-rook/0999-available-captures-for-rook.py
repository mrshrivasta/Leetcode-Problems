class Solution:
    def numRookCaptures(self, board):
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    ri, ci = i, j
        res = 0
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            r, c = ri, ci
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == 'B': break
                if board[r][c] == 'p': res += 1; break
                r += dr; c += dc
        return res