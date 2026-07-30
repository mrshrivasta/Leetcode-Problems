class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        v = set("aeiouAEIOU")
        mid = len(s) // 2
        return sum(c in v for c in s[:mid]) == sum(c in v for c in s[mid:])