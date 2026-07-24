class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        from functools import reduce
        return reduce(lambda a, b: a | b, nums) * (1 << (len(nums) - 1))