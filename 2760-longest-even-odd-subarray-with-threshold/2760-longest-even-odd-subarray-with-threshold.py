class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        res, n = 0, len(nums)
        for l in range(n):
            if nums[l] % 2 == 0 and nums[l] <= threshold:
                r = l
                while r + 1 < n and nums[r+1] % 2 != nums[r] % 2 and nums[r+1] <= threshold:
                    r += 1
                res = max(res, r - l + 1)
        return res