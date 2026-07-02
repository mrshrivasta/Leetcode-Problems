from collections import Counter

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)

        if pa == pb:
            return

        if self.size[pa] < self.size[pb]:
            pa, pb = pb, pa

        self.parent[pb] = pa
        self.size[pa] += self.size[pb]


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        dsu = DSU(n)
        factor_to_index = {}

        for i, num in enumerate(nums):
            x = num
            factor = 2

            while factor * factor <= x:
                if x % factor == 0:
                    if factor in factor_to_index:
                        dsu.union(i, factor_to_index[factor])
                    else:
                        factor_to_index[factor] = i

                    while x % factor == 0:
                        x //= factor

                factor += 1

            if x > 1:
                if x in factor_to_index:
                    dsu.union(i, factor_to_index[x])
                else:
                    factor_to_index[x] = i

        count = Counter(dsu.find(i) for i in range(n))
        return max(count.values())