class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        return [[max(grid[r][c] for r in range(i,i+3) for c in range(j,j+3)) for j in range(n-2)] for i in range(n-2)]