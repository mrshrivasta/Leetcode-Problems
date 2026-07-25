class Solution:
    def prefixesDivBy5(self, nums):
        res, cur = [], 0
        for n in nums:
            cur = (cur * 2 + n) % 5
            res.append(cur == 0)
        return res