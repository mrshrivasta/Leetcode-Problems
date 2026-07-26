class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        from collections import Counter

class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        freqs = sorted(Counter(s).values())
        return sum(freqs[:max(0, len(freqs) - k)])