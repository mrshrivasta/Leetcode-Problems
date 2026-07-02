class Solution:
    def stoneGameVII(self, stones):
        n = len(stones)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        dp = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1
                total = prefix[r + 1] - prefix[l]

                dp[l][r] = max(
                    total - stones[l] - dp[l + 1][r],
                    total - stones[r] - dp[l][r - 1]
                )

        return dp[0][n - 1]