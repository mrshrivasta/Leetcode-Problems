class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        flat = [x for row in grid for x in row]
        n2 = len(flat)
        c = Counter(flat)
        a = next(k for k, v in c.items() if v == 2)
        b = next(i for i in range(1, n2+1) if i not in c)
        return [a, b]