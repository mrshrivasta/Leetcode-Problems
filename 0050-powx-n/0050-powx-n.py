class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0

        while n > 0:
            if n % 2 == 1:        # odd exponent — peel off one factor
                result *= x
                n -= 1
            x *= x                # square the base
            n //= 2               # halve the exponent

        return result