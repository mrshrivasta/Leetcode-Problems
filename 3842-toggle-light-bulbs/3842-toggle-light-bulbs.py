class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        from collections import Counter
        return sorted(b for b, c in Counter(bulbs).items() if c % 2)