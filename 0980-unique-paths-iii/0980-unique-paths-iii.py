class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        empty = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != -1:
                    empty += 1
                if grid[r][c] == 1:
                    sr, sc = r, c

        def dfs(r, c, remain):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == -1:
                return 0

            if grid[r][c] == 2:
                return 1 if remain == 1 else 0

            temp = grid[r][c]
            grid[r][c] = -1

            paths = (
                dfs(r + 1, c, remain - 1) +
                dfs(r - 1, c, remain - 1) +
                dfs(r, c + 1, remain - 1) +
                dfs(r, c - 1, remain - 1)
            )

            grid[r][c] = temp
            return paths

        return dfs(sr, sc, empty)