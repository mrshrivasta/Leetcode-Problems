class Solution:
    def countNegatives(self, grid):
        return sum(n < 0 for row in grid for n in row)