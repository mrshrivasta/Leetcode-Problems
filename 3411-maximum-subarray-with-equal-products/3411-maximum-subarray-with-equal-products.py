class Solution:
    def maxLength(self, nums: List[int]) -> int:
        from math import gcd, lcm
        res, n = 1, len(nums)
        for i in range(n):
            p, g, l = 1, 0, 1
            for j in range(i, n):
                p *= nums[j]
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])
                if p == g * l:
                    res = max(res, j - i + 1)
        return res