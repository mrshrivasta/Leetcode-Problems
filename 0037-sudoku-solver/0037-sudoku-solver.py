class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows  = [set() for _ in range(9)]
        cols  = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Seed constraint sets and collect empty cells
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empty.append((r, c))
                else:
                    box_id = (r // 3) * 3 + (c // 3)
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_id].add(val)

        def backtrack(idx: int) -> bool:
            if idx == len(empty):
                return True   # all empty cells filled — solved

            r, c = empty[idx]
            box_id = (r // 3) * 3 + (c // 3)

            for digit in '123456789':
                if digit in rows[r] or digit in cols[c] or digit in boxes[box_id]:
                    continue   # constraint violation — skip

                # Place
                board[r][c] = digit
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[box_id].add(digit)

                if backtrack(idx + 1):
                    return True

                # Undo
                board[r][c] = '.'
                rows[r].remove(digit)
                cols[c].remove(digit)
                boxes[box_id].remove(digit)

            return False   # no digit worked — backtrack

        backtrack(0)