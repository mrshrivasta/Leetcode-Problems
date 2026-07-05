from typing import List

class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.sz = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)

        if rx == ry:
            return

        if self.sz[rx] < self.sz[ry]:
            rx, ry = ry, rx

        self.parent[ry] = rx
        self.sz[rx] += self.sz[ry]

    def size(self, x):
        return self.sz[self.find(x)]


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        copy = [row[:] for row in grid]

        for r, c in hits:
            if copy[r][c] == 1:
                copy[r][c] = 0

        roof = m * n
        dsu = DSU(m * n + 1)

        def index(r, c):
            return r * n + c

        for r in range(m):
            for c in range(n):
                if copy[r][c] != 1:
                    continue

                if r == 0:
                    dsu.union(index(r, c), roof)

                for dr, dc in [(1, 0), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < m and
                        0 <= nc < n and
                        copy[nr][nc] == 1
                    ):
                        dsu.union(index(r, c), index(nr, nc))

        ans = []

        for r, c in reversed(hits):
            if grid[r][c] == 0:
                ans.append(0)
                continue

            prev_roof = dsu.size(roof)

            copy[r][c] = 1

            if r == 0:
                dsu.union(index(r, c), roof)

            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < m and
                    0 <= nc < n and
                    copy[nr][nc] == 1
                ):
                    dsu.union(index(r, c), index(nr, nc))

            new_roof = dsu.size(roof)

            ans.append(max(0, new_roof - prev_roof - 1))

        return ans[::-1]