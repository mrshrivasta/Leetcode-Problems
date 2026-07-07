from collections import Counter

class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        c = Counter(str(n))
        return int(min(c, key=lambda x: (c[x], x)))