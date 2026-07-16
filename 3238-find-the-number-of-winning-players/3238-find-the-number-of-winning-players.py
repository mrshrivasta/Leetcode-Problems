class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        count = 0
        for i in range(n):
            c = Counter(y for x, y in pick if x == i)
            if c and max(c.values()) > i:
                count += 1
        return count