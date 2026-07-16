class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total, cap, count = sum(apple), 0, 0
        for c in sorted(capacity, reverse=True):
            cap += c; count += 1
            if cap >= total: return count