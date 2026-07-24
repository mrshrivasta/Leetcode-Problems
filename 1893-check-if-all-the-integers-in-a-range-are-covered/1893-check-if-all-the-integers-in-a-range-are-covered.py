class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        return all(any(s <= x <= e for s, e in ranges) for x in range(left, right + 1))