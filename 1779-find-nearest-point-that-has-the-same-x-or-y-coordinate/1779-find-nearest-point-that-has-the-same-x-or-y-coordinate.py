class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        best, res = float('inf'), -1
        for i, (a, b) in enumerate(points):
            if a == x or b == y:
                d = abs(x-a) + abs(y-b)
                if d < best:
                    best, res = d, i
        return res