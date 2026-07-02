class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = list(range(26))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            parent[find(a)] = find(b)

        for eq in equations:
            if eq[1] == '=':
                union(ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a'))

        for eq in equations:
            if eq[1] == '!':
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')

                if find(a) == find(b):
                    return False

        return True