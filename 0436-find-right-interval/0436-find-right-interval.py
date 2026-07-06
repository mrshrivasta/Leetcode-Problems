class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        from bisect import bisect_left
        starts = sorted((s, i) for i, (s, e) in enumerate(intervals))
        keys = [s for s, _ in starts]
        res = []
        for s, e in intervals:
            idx = bisect_left(keys, e)
            res.append(starts[idx][1] if idx < len(starts) else -1)
        return res