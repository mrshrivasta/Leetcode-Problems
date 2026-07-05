from typing import List

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        dp = [0.0] * n

        for i in range(n):
            dp[i] = (prefix[n] - prefix[i]) / (n - i)

        for _ in range(k - 1):
            new_dp = dp[:]

            for i in range(n):
                for j in range(i + 1, n):
                    avg = (prefix[j] - prefix[i]) / (j - i)
                    new_dp[i] = max(new_dp[i], avg + dp[j])

            dp = new_dp

        return dp[0]