class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        from collections import Counter
        c = Counter(nums)
        vals = sorted(c)
        for i, x in enumerate(vals):
            for y in vals[i+1:]:
                if c[x] != c[y]:
                    return [x, y]
        return [-1, -1]