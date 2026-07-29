from collections import Counter

class Solution:
    def similarPairs(self, words: list[str]) -> int:
        keys = [frozenset(w) for w in words]
        count = Counter(keys)
        return sum(v * (v-1) // 2 for v in count.values())