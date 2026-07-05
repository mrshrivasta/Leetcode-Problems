class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Initialize a 2D DP array with 0s
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for s in strs:
            # Count the number of 0s and 1s in the current string
            zeros = s.count('0')
            ones = s.count('1')
            
            # Update the DP table backwards to avoid using the same string multiple times
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    # dp[i][j] is the max of:
                    # 1. Not taking the current string: dp[i][j]
                    # 2. Taking the current string: dp[i - zeros][j - ones] + 1
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
                    
        return dp[m][n]