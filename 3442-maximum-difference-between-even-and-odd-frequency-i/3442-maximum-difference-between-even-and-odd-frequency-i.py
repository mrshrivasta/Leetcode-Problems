from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        odds = [v for v in count.values() if v % 2 == 1]
        evens = [v for v in count.values() if v % 2 == 0]
        return max(odds) - min(evens)