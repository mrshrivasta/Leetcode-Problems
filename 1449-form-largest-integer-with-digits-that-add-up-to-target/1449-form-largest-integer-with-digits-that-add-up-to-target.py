class Solution:
    def largestNumber(self, cost, target):
        dp = [-10**9] * (target + 1)
        dp[0] = 0

        for t in range(1, target + 1):
            for d in range(9):
                c = cost[d]
                if t >= c:
                    dp[t] = max(dp[t], dp[t - c] + 1)

        if dp[target] < 0:
            return "0"

        ans = []
        t = target

        for d in range(8, -1, -1):  # digit 9 -> 1
            c = cost[d]
            while t >= c and dp[t] == dp[t - c] + 1:
                ans.append(str(d + 1))
                t -= c

        return "".join(ans)