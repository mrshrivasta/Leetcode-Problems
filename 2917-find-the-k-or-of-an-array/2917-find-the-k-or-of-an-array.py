class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        return sum(1 << b for b in range(32) if sum(n >> b & 1 for n in nums) >= k)