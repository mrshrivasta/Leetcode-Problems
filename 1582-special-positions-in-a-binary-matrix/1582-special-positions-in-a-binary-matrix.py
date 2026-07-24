class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and sum(mat[i]) == 1 and sum(mat[r][j] for r in range(m)) == 1:
                    count += 1
        return count