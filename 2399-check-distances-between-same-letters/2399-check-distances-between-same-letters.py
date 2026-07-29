class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        pos = {}
        for i, c in enumerate(s):
            if c in pos:
                if i - pos[c] - 1 != distance[ord(c) - ord('a')]:
                    return False
            else:
                pos[c] = i
        return True