class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        mn, mx = min(nums), max(nums)
        if mn == mx: return 0
        n = len(nums)
        size = max(1, (mx-mn)//(n-1))
        buckets = [[float('inf'), float('-inf')] for _ in range((mx-mn)//size + 1)]
        for x in nums:
            i = (x-mn)//size
            buckets[i][0] = min(buckets[i][0], x)
            buckets[i][1] = max(buckets[i][1], x)
        res, prev = 0, mn
        for lo, hi in buckets:
            if lo == float('inf'): continue
            res = max(res, lo-prev)
            prev = hi
        return res