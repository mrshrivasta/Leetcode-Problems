from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        need = Counter(c.lower() for c in licensePlate if c.isalpha())
        return min((w for w in words if not need - Counter(w)), key=len)