class Solution:
    def kConcatenationMaxSum(self, arr, k):
        MOD = 10**9 + 7

        def kadane(nums):
            cur = best = 0
            for x in nums:
                cur = max(x, cur + x)
                best = max(best, cur)
            return best

        total = sum(arr)
        if k == 1:
            return kadane(arr) % MOD

        double = arr * 2
        best_two = kadane(double)

        if total > 0:
            return (best_two + (k - 2) * total) % MOD
        else:
            return best_two % MOD