class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        res, mn = [], float('inf')
        for c in cost:
            mn = min(mn, c)
            res.append(mn)
        return res