from collections import Counter

class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        count = Counter(''.join(words))
        return all(v % len(words) == 0 for v in count.values())