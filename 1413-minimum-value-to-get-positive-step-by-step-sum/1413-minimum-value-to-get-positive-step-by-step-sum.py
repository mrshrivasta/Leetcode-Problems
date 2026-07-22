class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_sum = min(accumulate(nums))
        return max(1, 1 - min_sum)