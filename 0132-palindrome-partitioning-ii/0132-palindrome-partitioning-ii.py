class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or is_pal[i+1][j-1]):
                    is_pal[i][j] = True

        dp = list(range(-1, n))
        for i in range(1, n):
            for j in range(i + 1):
                if is_pal[j][i]:
                    dp[i+1] = min(dp[i+1], dp[j] + 1)

        return dp[n]