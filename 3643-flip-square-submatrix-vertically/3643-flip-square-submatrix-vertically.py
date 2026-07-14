class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        sub = [row[y:y+k] for row in grid[x:x+k]]
        sub.reverse()
        for i in range(k):
            grid[x+i][y:y+k] = sub[i]
        return grid