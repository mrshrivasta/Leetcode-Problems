class Solution:
    def updateBoard(self, board, click):
        from collections import deque

        m, n = len(board), len(board[0])
        r, c = click

        dirs = [(-1,-1), (-1,0), (-1,1),
                (0,-1),         (0,1),
                (1,-1), (1,0),  (1,1)]

        def count_mines(x, y):
            cnt = 0
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'M':
                    cnt += 1
            return cnt

        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board

        q = deque([(r, c)])

        while q:
            x, y = q.popleft()

            if board[x][y] != 'E':
                continue

            mines = count_mines(x, y)

            if mines > 0:
                board[x][y] = str(mines)
            else:
                board[x][y] = 'B'
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'E':
                        q.append((nx, ny))

        return board