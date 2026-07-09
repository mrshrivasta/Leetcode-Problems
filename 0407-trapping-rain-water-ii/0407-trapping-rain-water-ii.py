from typing import List
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []

        for r in range(m):
            for c in [0, n - 1]:
                heapq.heappush(heap, (heightMap[r][c], r, c))
                visited[r][c] = True

        for c in range(1, n - 1):
            for r in [0, m - 1]:
                heapq.heappush(heap, (heightMap[r][c], r, c))
                visited[r][c] = True

        water = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            height, r, c = heapq.heappop(heap)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True

                    water += max(0, height - heightMap[nr][nc])

                    heapq.heappush(
                        heap,
                        (max(height, heightMap[nr][nc]), nr, nc)
                    )

        return water