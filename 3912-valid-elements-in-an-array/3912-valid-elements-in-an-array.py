class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        pre = [0] * n
        suf = [0] * n
        pre[0] = nums[0]
        suf[-1] = nums[-1]
        for i in range(1, n):
            pre[i] = max(pre[i-1], nums[i])
        for i in range(n-2, -1, -1):
            suf[i] = max(suf[i+1], nums[i])
        return [nums[i] for i in range(n) if i == 0 or i == n-1 or nums[i] > pre[i-1] or nums[i] > suf[i+1]]