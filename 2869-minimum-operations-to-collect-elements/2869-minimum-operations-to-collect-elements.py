class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        need, ops = set(range(1, k+1)), 0
        for x in reversed(nums):
            ops += 1
            need.discard(x)
            if not need: return ops