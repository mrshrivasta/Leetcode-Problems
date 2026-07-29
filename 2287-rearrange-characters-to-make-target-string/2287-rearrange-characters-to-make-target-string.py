from collections import Counter

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        cs, ct = Counter(s), Counter(target)
        return min(cs[c] // ct[c] for c in ct)