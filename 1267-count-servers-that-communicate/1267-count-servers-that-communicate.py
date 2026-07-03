from collections import Counter

class Solution:
    def countServers(self, grid):
        m, n = len(grid), len(grid[0])

        row = Counter()
        col = Counter()
        servers = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
                    servers.append((i, j))

        ans = 0
        for i, j in servers:
            if row[i] > 1 or col[j] > 1:
                ans += 1

        return ans