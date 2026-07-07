class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for n in s:
            if n-1 not in s:
                cur = 1
                while n+cur in s:
                    cur += 1
                res = max(res, cur)
        return res