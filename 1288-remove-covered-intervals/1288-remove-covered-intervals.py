class Solution:
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        prev_end = 0

        for s, e in intervals:
            if e > prev_end:
                count += 1
                prev_end = e

        return count