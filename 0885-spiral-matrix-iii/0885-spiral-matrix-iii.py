class Solution:
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        res = []
        r, c = rStart, cStart

        if 0 <= r < rows and 0 <= c < cols:
            res.append([r, c])

        steps = 1
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while len(res) < rows * cols:
            for d in range(4):
                dr, dc = dirs[d]
                move = steps

                for _ in range(move):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])

                if d % 2 == 1:
                    steps += 1

        return res