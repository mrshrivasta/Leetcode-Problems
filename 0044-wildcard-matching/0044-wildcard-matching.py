class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Base case: empty string matches empty pattern
        dp[0][0] = True

        # Base case: empty string vs pattern — only '*'s can match empty
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]   # '*' matches zero characters

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # Match zero chars: dp[i][j-1]  (skip the '*')
                    # Match one+ chars: dp[i-1][j]  (consume one s char, keep '*')
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    # Single character match — inherit diagonal
                    dp[i][j] = dp[i - 1][j - 1]

                # else: mismatch → stays False

        return dp[m][n]