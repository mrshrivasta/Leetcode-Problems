class Solution:
    def dayOfYear(self, date: str) -> int:
        y, m, d = int(date[:4]), int(date[5:7]), int(date[8:])
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
            days[1] = 29
        return sum(days[:m-1]) + d