class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0

        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i]) + carry
            if bit % 2 == 1:  # odd: add 1 (costs 1 step) + divide by 2 (costs 1 step)
                steps += 2
                carry = 1
            else:             # even: just divide by 2 (costs 1 step)
                steps += 1

        return steps + carry  # handle any remaining carry at position 0