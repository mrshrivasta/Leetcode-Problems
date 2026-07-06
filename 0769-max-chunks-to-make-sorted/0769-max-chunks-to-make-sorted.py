from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        max_so_far = 0

        for i, num in enumerate(arr):
            max_so_far = max(max_so_far, num)

            if max_so_far == i:
                chunks += 1

        return chunks