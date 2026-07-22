class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        s = set(range(1, n+1))
        return all(set(row) == s for row in matrix) and all(set(matrix[r][c] for r in range(n)) == s for c in range(n))