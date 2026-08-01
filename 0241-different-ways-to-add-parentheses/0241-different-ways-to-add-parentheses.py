class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}

        def solve(expr):
            if expr in memo:
                return memo[expr]
            if expr.isdigit() or (len(expr) <= 2 and expr.lstrip('-').isdigit()):
                return [int(expr)]

            results = []
            for i, char in enumerate(expr):
                if char in '+-*':
                    left  = solve(expr[:i])
                    right = solve(expr[i+1:])
                    for l in left:
                        for r in right:
                            if char == '+': results.append(l + r)
                            elif char == '-': results.append(l - r)
                            elif char == '*': results.append(l * r)

            memo[expr] = results
            return results

        return solve(expression)