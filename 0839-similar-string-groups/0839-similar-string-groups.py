class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            parent[find(x)] = find(y)

        def is_similar(a, b):
            diffs = [(c1, c2) for c1, c2 in zip(a, b) if c1 != c2]
            return len(diffs) == 0 or (len(diffs) == 2 and diffs[0] == diffs[1][::-1])

        for i in range(n):
            for j in range(i + 1, n):
                if find(i) != find(j) and is_similar(strs[i], strs[j]):
                    union(i, j)

        return sum(parent[i] == i for i in range(n))