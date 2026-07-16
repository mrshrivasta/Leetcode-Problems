class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        res, max_t = events[0][0], events[0][1]
        for i in range(1, len(events)):
            t = events[i][1] - events[i-1][1]
            if t > max_t or (t == max_t and events[i][0] < res):
                max_t, res = t, events[i][0]
        return res