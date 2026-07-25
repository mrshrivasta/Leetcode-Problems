class Solution:
    def minimumFlips(self, n: int) -> int:
        s = bin(n)[2:]
        return sum(a != b for a, b in zip(s, s[::-1]))