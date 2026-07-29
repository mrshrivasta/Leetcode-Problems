class Solution:
    def countAsterisks(self, s: str) -> int:
        return sum(seg.count('*') for seg in s.split('|')[::2])