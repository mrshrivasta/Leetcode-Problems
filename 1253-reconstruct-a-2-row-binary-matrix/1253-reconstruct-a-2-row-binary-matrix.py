class Solution:
    def reconstructMatrix(self, upper, lower, colsum):
        n = len(colsum)
        res = [[0] * n, [0] * n]

        for i in range(n):
            if colsum[i] == 2:
                res[0][i] = 1
                res[1][i] = 1
                upper -= 1
                lower -= 1
            elif colsum[i] == 1:
                if upper > lower:
                    res[0][i] = 1
                    upper -= 1
                else:
                    res[1][i] = 1
                    lower -= 1

            if upper < 0 or lower < 0:
                return []

        if upper != 0 or lower != 0:
            return []

        return res