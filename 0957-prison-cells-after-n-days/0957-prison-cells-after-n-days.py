class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {}

        while n:
            state = tuple(cells)

            if state in seen:
                cycle = seen[state] - n
                n %= cycle

            seen[state] = n

            if n > 0:
                n -= 1
                nxt = [0] * 8

                for i in range(1, 7):
                    nxt[i] = 1 if cells[i - 1] == cells[i + 1] else 0

                cells = nxt

        return cells