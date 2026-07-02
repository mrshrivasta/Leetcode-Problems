class Solution:
    def getSumAbsoluteDifferences(self, nums):
        n = len(nums)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        res = []

        for i in range(n):
            left = nums[i] * i - prefix[i]
            right = (prefix[n] - prefix[i + 1]) - nums[i] * (n - i - 1)
            res.append(left + right)

        return res