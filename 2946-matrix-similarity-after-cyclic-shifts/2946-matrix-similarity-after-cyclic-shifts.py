class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        for i, row in enumerate(mat):
            n = len(row)
            s = k % n
            shifted = row[-s:] + row[:-s] if i % 2 else row[s:] + row[:s]
            if shifted != row:
                return False
        return True