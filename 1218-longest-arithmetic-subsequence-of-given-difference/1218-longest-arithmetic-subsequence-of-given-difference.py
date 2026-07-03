class Solution:
    def longestSubsequence(self, arr, difference):
        dp = {}
        ans = 0

        for x in arr:
            dp[x] = dp.get(x - difference, 0) + 1
            ans = max(ans, dp[x])

        return ans