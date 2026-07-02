from collections import defaultdict
from math import gcd
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        ans = 0

        for i in range(n):
            slopes = defaultdict(int)
            cur_max = 0

            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                g = gcd(dx, dy)
                dx //= g
                dy //= g

                if dx < 0:
                    dx = -dx
                    dy = -dy

                if dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1

                slopes[(dy, dx)] += 1
                cur_max = max(cur_max, slopes[(dy, dx)])

            ans = max(ans, cur_max + 1)

        return ans