class Solution:
    def sumZero(self, n):
        res = list(range(1, n))
        return res + [-sum(res)]