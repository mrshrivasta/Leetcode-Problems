class Solution:
    def leastBricks(self, wall):
        from collections import defaultdict

        edges = defaultdict(int)

        for row in wall:
            prefix = 0
            for i in range(len(row) - 1):
                prefix += row[i]
                edges[prefix] += 1

        if not edges:
            return len(wall)

        return len(wall) - max(edges.values())