from typing import List
from functools import lru_cache

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]],
                m: int, n: int, target: int) -> int:

        INF = float('inf')

        @lru_cache(None)
        def dfs(i, prev_color, groups):
            if groups > target:
                return INF

            if i == m:
                return 0 if groups == target else INF

            if houses[i] != 0:
                new_groups = groups + (houses[i] != prev_color)
                return dfs(i + 1, houses[i], new_groups)

            ans = INF

            for color in range(1, n + 1):
                new_groups = groups + (color != prev_color)

                ans = min(
                    ans,
                    cost[i][color - 1] +
                    dfs(i + 1, color, new_groups)
                )

            return ans

        res = dfs(0, 0, 0)
        return -1 if res == INF else res