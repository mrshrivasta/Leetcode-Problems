class Solution:
    def kWeakestRows(self, mat, k):
        return sorted(range(len(mat)), key=lambda i: sum(mat[i]))[:k]