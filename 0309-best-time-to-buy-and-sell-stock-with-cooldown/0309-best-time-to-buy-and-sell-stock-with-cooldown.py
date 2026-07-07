class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = float('-inf')
        sold = cool = 0
        for p in prices:
            hold, sold, cool = max(hold, cool-p), hold+p, max(cool, sold)
        return max(sold, cool)