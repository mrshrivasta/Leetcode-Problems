from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cost = [[0] * k for _ in nums]

        for i, v in enumerate(nums):
            r = v % k

            for t in range(k):
                d = abs(r - t)
                cost[i][t] = min(d, k - d)

        ans = float('inf')

        for x in range(k):
            even_cost = sum(cost[i][x] for i in range(0, len(nums), 2))

            for y in range(k):
                if x == y:
                    continue

                cur = even_cost

                for i in range(1, len(nums), 2):
                    cur += cost[i][y]

                ans = min(ans, cur)

        return ans