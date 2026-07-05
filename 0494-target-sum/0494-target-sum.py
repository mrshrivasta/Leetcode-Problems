class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total_sum = sum(nums)
        
        # Quick edge cases check
        if abs(target) > total_sum or (total_sum + target) % 2 != 0:
            return 0
            
        subset_target = (total_sum + target) // 2
        
        # dp[i] will store the number of subsets that sum to i
        dp = [0] * (subset_target + 1)
        dp[0] = 1 # There is exactly 1 way to make a sum of 0 (the empty set)
        
        # Fill the DP table
        for num in nums:
            # Iterate backwards to avoid using the same element multiple times
            for i in range(subset_target, num - 1, -1):
                dp[i] += dp[i - num]
                
        return dp[subset_target]