class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        res, skip = [], False
        for i, row in enumerate(grid):
            cells = row if i % 2 == 0 else row[::-1]
            for x in cells:
                if not skip: res.append(x)
                skip = not skip
        return res