class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        def toDays(date):
            m, d = int(date[:2]), int(date[3:])
            return sum(days[:m-1]) + d
        start = max(toDays(arriveAlice), toDays(arriveBob))
        end = min(toDays(leaveAlice), toDays(leaveBob))
        return max(0, end - start + 1)