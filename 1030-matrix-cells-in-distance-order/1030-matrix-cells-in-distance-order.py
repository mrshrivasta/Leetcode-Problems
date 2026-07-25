class Solution:
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        return sorted([(r,c) for r in range(rows) for c in range(cols)],
                      key=lambda x: abs(x[0]-rCenter) + abs(x[1]-cCenter))