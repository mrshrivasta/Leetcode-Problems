class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current: List[str], open: int, close: int) -> None:
            if len(current) == 2 * n:
                result.append("".join(current))
                return

            if open < n:
                current.append('(')
                backtrack(current, open + 1, close)
                current.pop()

            if close < open:
                current.append(')')
                backtrack(current, open, close + 1)
                current.pop()

        backtrack([], 0, 0)
        return result