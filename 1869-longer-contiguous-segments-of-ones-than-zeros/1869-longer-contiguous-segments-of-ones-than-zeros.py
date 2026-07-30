class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max_ones = max(len(x) for x in s.split('0'))
        max_zeros = max(len(x) for x in s.split('1'))
        return max_ones > max_zeros