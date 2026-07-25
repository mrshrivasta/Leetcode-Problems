class Solution:
    def oddCells(self, m, n, indices):
        rows, cols = [0]*m, [0]*n
        for r, c in indices:
            rows[r] += 1
            cols[c] += 1
        return sum((rows[i]+cols[j]) % 2 for i in range(m) for j in range(n))