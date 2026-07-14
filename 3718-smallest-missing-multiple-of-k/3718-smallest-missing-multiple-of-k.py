class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s, x = set(nums), k
        while x in s:
            x += k
        return x