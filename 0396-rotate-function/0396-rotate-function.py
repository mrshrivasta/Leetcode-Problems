class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        f = sum(i*v for i, v in enumerate(nums))
        res = f
        for i in range(1, n):
            f += s - n*nums[n-i]
            res = max(res, f)
        return res