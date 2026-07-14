from itertools import combinations
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)
        res = float('inf')
        for indices in pos.values():
            if len(indices) >= 3:
                for i, j, k in combinations(indices, 3):
                    res = min(res, abs(i-j)+abs(j-k)+abs(k-i))
        return res if res != float('inf') else -1