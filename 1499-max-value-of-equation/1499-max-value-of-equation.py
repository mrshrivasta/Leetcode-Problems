from typing import List
from collections import deque

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        dq = deque()  # (yi - xi, xi)
        ans = float('-inf')

        for x, y in points:

            while dq and x - dq[0][1] > k:
                dq.popleft()

            if dq:
                ans = max(ans, x + y + dq[0][0])

            value = y - x

            while dq and dq[-1][0] <= value:
                dq.pop()

            dq.append((value, x))

        return ans