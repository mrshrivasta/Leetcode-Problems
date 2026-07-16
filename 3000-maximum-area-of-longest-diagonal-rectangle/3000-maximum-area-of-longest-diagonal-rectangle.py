class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        return max(dimensions, key=lambda d: (d[0]**2 + d[1]**2, d[0]*d[1]))[0] * max(dimensions, key=lambda d: (d[0]**2 + d[1]**2, d[0]*d[1]))[1]