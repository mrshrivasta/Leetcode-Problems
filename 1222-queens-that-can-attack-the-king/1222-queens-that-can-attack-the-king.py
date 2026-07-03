class Solution:
    def queensAttacktheKing(self, queens, king):
        board = set(map(tuple, queens))
        xk, yk = king

        directions = [
            (1,0), (-1,0), (0,1), (0,-1),
            (1,1), (1,-1), (-1,1), (-1,-1)
        ]

        res = []

        for dx, dy in directions:
            x, y = xk + dx, yk + dy

            while 0 <= x < 8 and 0 <= y < 8:
                if (x, y) in board:
                    res.append([x, y])
                    break
                x += dx
                y += dy

        return res