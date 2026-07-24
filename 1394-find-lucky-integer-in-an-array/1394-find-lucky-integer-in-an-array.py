from collections import Counter

class Solution:
    def findLucky(self, arr):
        c = Counter(arr)
        return max((n for n in c if c[n] == n), default=-1)