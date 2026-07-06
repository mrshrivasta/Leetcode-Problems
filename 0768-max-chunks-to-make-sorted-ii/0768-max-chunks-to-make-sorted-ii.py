from typing import List
from collections import Counter

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sorted_arr = sorted(arr)

        cnt = Counter()
        chunks = 0

        for a, b in zip(arr, sorted_arr):
            cnt[a] += 1
            if cnt[a] == 0:
                del cnt[a]

            cnt[b] -= 1
            if cnt[b] == 0:
                del cnt[b]

            if not cnt:
                chunks += 1

        return chunks