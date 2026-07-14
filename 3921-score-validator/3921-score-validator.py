class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score = counter = 0
        for e in events:
            if counter == 10:
                break
            if e == "W":
                counter += 1
            elif e in ("WD", "NB"):
                score += 1
            else:
                score += int(e)
        return [score, counter]