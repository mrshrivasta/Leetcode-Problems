class Solution:
    def heightChecker(self, heights):
        return sum(a != b for a, b in zip(heights, sorted(heights)))