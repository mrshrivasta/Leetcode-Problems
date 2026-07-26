class Solution:
    def maxFreqSum(self, s: str) -> int:
        from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set('aeiou')
        count = Counter(s)
        v = max((f for c, f in count.items() if c in vowels), default=0)
        c = max((f for c, f in count.items() if c not in vowels), default=0)
        return v + c