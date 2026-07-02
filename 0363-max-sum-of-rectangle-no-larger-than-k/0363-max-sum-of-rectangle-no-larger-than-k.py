from typing import List
from bisect import bisect_left, insort

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = float('-inf')

        for left in range(n):
            row_sums = [0] * m

            for right in range(left, n):
                for r in range(m):
                    row_sums[r] += matrix[r][right]

                prefix = 0
                prefixes = [0]

                for s in row_sums:
                    prefix += s

                    idx = bisect_left(prefixes, prefix - k)
                    if idx < len(prefixes):
                        ans = max(ans, prefix - prefixes[idx])

                    insort(prefixes, prefix)

        return ans