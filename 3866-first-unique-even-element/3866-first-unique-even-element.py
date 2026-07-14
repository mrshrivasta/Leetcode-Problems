class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        from collections import Counter
        c = Counter(x for x in nums if x % 2 == 0)
        return next((x for x in nums if x % 2 == 0 and c[x] == 1), -1)