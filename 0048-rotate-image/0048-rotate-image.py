class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Step 1: Transpose — swap matrix[i][j] with matrix[j][i]
        for i in range(n):
            for j in range(i + 1, n):    # upper triangle only (avoid double-swap)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()