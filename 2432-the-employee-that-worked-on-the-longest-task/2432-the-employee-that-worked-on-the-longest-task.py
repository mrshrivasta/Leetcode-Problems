class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        res, max_time, prev = 0, 0, 0
        for eid, t in logs:
            dur = t - prev
            if dur > max_time or (dur == max_time and eid < res):
                max_time, res = dur, eid
            prev = t
        return res