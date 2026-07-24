class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        mins = [min(l, w) for l, w in rectangles]
        maxLen = max(mins)
        return mins.count(maxLen)