from typing import List
from functools import lru_cache

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:

        @lru_cache(None)
        def dfs(needs_tuple):
            needs_list = list(needs_tuple)

            # Buy everything individually
            min_cost = sum(needs_list[i] * price[i] for i in range(len(price)))

            # Try each special offer
            for offer in special:
                new_needs = []

                for i in range(len(price)):
                    if offer[i] > needs_list[i]:
                        break
                    new_needs.append(needs_list[i] - offer[i])
                else:
                    min_cost = min(
                        min_cost,
                        offer[-1] + dfs(tuple(new_needs))
                    )

            return min_cost

        return dfs(tuple(needs))