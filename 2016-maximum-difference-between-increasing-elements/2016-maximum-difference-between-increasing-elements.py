class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_val, res = nums[0], -1
        for x in nums[1:]:
            if x > min_val:
                res = max(res, x - min_val)
            min_val = min(min_val, x)
        return res