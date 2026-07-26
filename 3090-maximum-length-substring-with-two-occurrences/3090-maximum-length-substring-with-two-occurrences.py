from collections import Counter

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l, best = 0, 0
        count = Counter()
        for r in range(len(s)):
            count[s[r]] += 1
            while count[s[r]] > 2:
                count[s[l]] -= 1
                l += 1
            best = max(best, r - l + 1)
        return best