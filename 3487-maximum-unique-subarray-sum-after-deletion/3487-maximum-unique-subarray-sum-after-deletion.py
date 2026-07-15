class Solution:
    def maxSum(self, nums: List[int]) -> int:
        return sum(x for x in set(nums) if x > 0) or max(nums)