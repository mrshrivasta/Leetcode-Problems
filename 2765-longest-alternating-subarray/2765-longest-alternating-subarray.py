class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        res = -1
        for l in range(len(nums)):
            for r in range(l+1, len(nums)):
                if nums[r] - nums[r-1] == (1 if (r-l) % 2 == 1 else -1):
                    res = max(res, r - l + 1)
                else:
                    break
        return res