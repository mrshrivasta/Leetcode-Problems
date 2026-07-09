from typing import List
from collections import Counter

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)

        if m == n:
            return n

        length = [0] * (n + 2)
        count = Counter()

        ans = -1

        for step, pos in enumerate(arr, 1):
            left = length[pos - 1]
            right = length[pos + 1]

            total = left + right + 1

            if left:
                count[left] -= 1
            if right:
                count[right] -= 1

            count[total] += 1

            length[pos - left] = total
            length[pos + right] = total

            if count[m] > 0:
                ans = step

        return ans