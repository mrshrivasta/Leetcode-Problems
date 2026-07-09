from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        heights = [0] * n
        ans = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            for j in range(n):
                mn = heights[j]

                for k in range(j, -1, -1):
                    mn = min(mn, heights[k])

                    if mn == 0:
                        break

                    ans += mn

        return ans