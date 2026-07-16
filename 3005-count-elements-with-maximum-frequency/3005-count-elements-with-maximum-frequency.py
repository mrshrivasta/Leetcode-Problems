class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        mx = max(c.values())
        return sum(v for v in c.values() if v == mx)