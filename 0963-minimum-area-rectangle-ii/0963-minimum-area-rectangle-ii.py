from collections import defaultdict
from math import sqrt

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        n = len(points)
        diagonals = defaultdict(list)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]

                midx = x1 + x2
                midy = y1 + y2
                dist = (x1 - x2) ** 2 + (y1 - y2) ** 2

                diagonals[(midx, midy, dist)].append((i, j))

        ans = float('inf')

        for pairs in diagonals.values():
            m = len(pairs)

            for i in range(m):
                p1, p2 = pairs[i]
                x1, y1 = points[p1]
                x2, y2 = points[p2]

                for j in range(i + 1, m):
                    p3, p4 = pairs[j]
                    x3, y3 = points[p3]

                    side1 = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
                    side2 = sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)

                    ans = min(ans, side1 * side2)

        return 0 if ans == float('inf') else ans