class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg = sum(nums) / len(nums)
        s = set(nums)
        x = max(1, int(avg) + 1)
        while x in s or x <= avg:
            x += 1
        return x