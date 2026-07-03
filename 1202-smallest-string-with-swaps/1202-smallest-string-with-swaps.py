class Solution:
    def smallestStringWithSwaps(self, s, pairs):
        n = len(s)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pa] = pb

        for a, b in pairs:
            union(a, b)

        from collections import defaultdict

        groups = defaultdict(list)

        for i in range(n):
            groups[find(i)].append(i)

        res = list(s)

        for idxs in groups.values():
            chars = sorted(s[i] for i in idxs)
            idxs.sort()
            for i, ch in zip(idxs, chars):
                res[i] = ch

        return "".join(res)