from collections import Counter
from math import isqrt

class Solution:
    def numSquarefulPerms(self, nums):
        count = Counter(nums)

        # Build graph
        graph = {x: [] for x in count}

        for x in count:
            for y in count:
                s = x + y
                r = isqrt(s)
                if r * r == s:
                    graph[x].append(y)

        n = len(nums)

        def dfs(x, remaining):
            count[x] -= 1

            if remaining == 0:
                count[x] += 1
                return 1

            ans = 0
            for nei in graph[x]:
                if count[nei]:
                    ans += dfs(nei, remaining - 1)

            count[x] += 1
            return ans

        result = 0

        for x in count:
            result += dfs(x, n - 1)

        return result