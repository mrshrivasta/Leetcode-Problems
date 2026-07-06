from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6

        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPS

            n = len(nums)

            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue

                    remaining = [
                        nums[k]
                        for k in range(n)
                        if k != i and k != j
                    ]

                    a, b = nums[i], nums[j]

                    for val in [a + b, a - b, a * b]:
                        if dfs(remaining + [val]):
                            return True

                    if abs(b) > EPS:
                        if dfs(remaining + [a / b]):
                            return True

            return False

        return dfs([float(x) for x in cards])