class Solution:
    def getMaximumGold(self, grid):
        m, n = len(grid), len(grid[0])
        ans = 0

        def dfs(x, y):
            gold = grid[x][y]
            grid[x][y] = 0

            best = 0
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                    best = max(best, dfs(nx, ny))

            grid[x][y] = gold
            return gold + best

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    ans = max(ans, dfs(i, j))

        return ans