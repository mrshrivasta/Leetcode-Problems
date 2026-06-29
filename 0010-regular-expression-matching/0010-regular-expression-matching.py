class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # dp[i][j] = does s[:i] match p[:j]?
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Base case: empty string matches empty pattern
        dp[0][0] = True

        # Base case: empty string vs pattern e.g. "a*b*c*"
        # A "x*" pair can match zero characters, extending the empty match
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # Option 1: use zero of the preceding element (skip "x*")
                    zero_match = dp[i][j - 2]

                    # Option 2: use one more of the preceding element
                    # Only valid if preceding pattern char matches current s char
                    preceding_matches = p[j - 2] == s[i - 1] or p[j - 2] == '.'
                    one_more_match = dp[i - 1][j] if preceding_matches else False

                    dp[i][j] = zero_match or one_more_match

                elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    # Current chars match — inherit diagonal
                    dp[i][j] = dp[i - 1][j - 1]

                # else: mismatch → stays False

        return dp[m][n]