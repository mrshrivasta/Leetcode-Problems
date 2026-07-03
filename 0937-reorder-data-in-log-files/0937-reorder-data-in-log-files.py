class Solution:
    def reorderLogFiles(self, logs):
        letters = []
        digits = []

        for log in logs:
            id_, rest = log.split(" ", 1)
            if rest[0].isdigit():
                digits.append(log)
            else:
                letters.append((rest, id_))

        letters.sort(key=lambda x: (x[0], x[1]))

        return [f"{i} {r}" for r, i in letters] + digits