class Solution:
    def minDeletionSize(self, strs):
        m = len(strs)
        n = len(strs[0])

        dp = [1] * n
        longest = 1

        for j in range(n):
            for i in range(j):
                valid = True

                for row in range(m):
                    if strs[row][i] > strs[row][j]:
                        valid = False
                        break

                if valid:
                    dp[j] = max(dp[j], dp[i] + 1)

            longest = max(longest, dp[j])

        return n - longest