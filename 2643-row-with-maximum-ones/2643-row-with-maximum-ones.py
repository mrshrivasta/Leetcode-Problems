class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        idx, mx = max(enumerate(mat), key=lambda x: sum(x[1]))
        return [idx, sum(mx)]