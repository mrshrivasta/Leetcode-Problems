class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        lo, hi = 0, n
        while lo < hi:
            mid = (lo+hi+1)//2
            if citations[n-mid] >= mid: lo = mid
            else: hi = mid-1
        return lo