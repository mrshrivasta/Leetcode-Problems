class Solution:
    def minSubsequence(self, nums):
        nums.sort(reverse=True)
        total, curr, res = sum(nums), 0, []
        for n in nums:
            curr += n
            res.append(n)
            if curr > total - curr:
                return res