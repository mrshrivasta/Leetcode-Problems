from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        best = -1

        for h1, h2, m1, m2 in permutations(arr):
            hour = h1 * 10 + h2
            minute = m1 * 10 + m2

            if hour < 24 and minute < 60:
                best = max(best, hour * 60 + minute)

        if best == -1:
            return ""

        return f"{best // 60:02d}:{best % 60:02d}"