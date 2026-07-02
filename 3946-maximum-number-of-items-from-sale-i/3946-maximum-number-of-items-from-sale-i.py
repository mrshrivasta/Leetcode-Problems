from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        gain = [0] * n
        for i in range(n):
            fi = items[i][0]
            cnt = 0
            for j in range(n):
                if i != j and items[j][0] % fi == 0:
                    cnt += 1
            gain[i] = cnt

        cheapest = min(price for _, price in items)

        dp = [-10**18] * (budget + 1)
        dp[0] = 0

        for i in range(n):
            price = items[i][1]
            value = 1 + gain[i]  # first purchased copy + free copies

            for b in range(budget, price - 1, -1):
                dp[b] = max(dp[b], dp[b - price] + value)

        ans = 0

        for spent in range(budget + 1):
            if dp[spent] < 0:
                continue

            remaining = budget - spent
            ans = max(ans, dp[spent] + remaining // cheapest)

        return ans