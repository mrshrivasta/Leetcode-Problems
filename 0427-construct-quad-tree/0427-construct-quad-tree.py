class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(r, c, size):
            val = grid[r][c]
            if all(grid[r+i][c+j] == val for i in range(size) for j in range(size)):
                return Node(val, True, None, None, None, None)
            half = size // 2
            return Node(1, False,
                build(r, c, half),
                build(r, c+half, half),
                build(r+half, c, half),
                build(r+half, c+half, half))
        return build(0, 0, len(grid))