class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = set('aeiou')
        v = sum(1 for c in s if c in vowels)
        c = sum(1 for c in s if c.isalpha() and c not in vowels)
        return v // c if c > 0 else 0