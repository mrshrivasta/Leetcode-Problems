class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        s = sorted(nums)
        return sum(s[-k:]) - sum(s[:k])