class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        return [max(len(str(grid[r][c])) for r in range(len(grid))) for c in range(len(grid[0]))]