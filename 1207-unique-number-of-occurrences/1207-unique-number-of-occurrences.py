from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr):
        c = Counter(arr).values()
        return len(c) == len(set(c))