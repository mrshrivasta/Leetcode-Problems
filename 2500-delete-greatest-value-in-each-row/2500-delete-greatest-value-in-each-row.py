class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()
        return sum(max(grid[r][c] for r in range(len(grid))) for c in range(len(grid[0])))