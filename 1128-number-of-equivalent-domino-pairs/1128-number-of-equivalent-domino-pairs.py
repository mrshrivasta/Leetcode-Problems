from collections import Counter

class Solution:
    def numEquivDominoPairs(self, dominoes):
        count = Counter(tuple(sorted(d)) for d in dominoes)
        return sum(v * (v-1) // 2 for v in count.values())