class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        from collections import Counter
        c = Counter(digits)
        res = []
        for n in range(100, 1000, 2):
            if Counter(int(d) for d in str(n)) <= c:
                res.append(n)
        return res