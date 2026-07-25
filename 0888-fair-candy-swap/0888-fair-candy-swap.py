class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2
        bobSet = set(bobSizes)
        for a in aliceSizes:
            if a - diff in bobSet:
                return [a, a - diff]