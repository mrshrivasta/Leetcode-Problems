from typing import List

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7

        sums = []

        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += nums[j]
                sums.append(curr)

        sums.sort()

        return sum(sums[left - 1:right]) % MOD