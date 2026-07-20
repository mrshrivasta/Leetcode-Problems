class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        s = sorted(nums)
        return s[1] if len(s) > 2 else -1