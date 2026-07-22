class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        keys = [j for j, x in enumerate(nums) if x == key]
        return [i for i in range(len(nums)) if any(abs(i-j) <= k for j in keys)]