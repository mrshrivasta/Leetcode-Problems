class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        m = max(candies)
        return [c + extraCandies >= m for c in candies]