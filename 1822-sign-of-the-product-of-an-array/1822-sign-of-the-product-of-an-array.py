class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums: return 0
        neg = sum(1 for x in nums if x < 0)
        return -1 if neg % 2 else 1