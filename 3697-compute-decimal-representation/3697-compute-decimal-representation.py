class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        res, power = [], 1
        while n:
            d = n % 10
            if d: res.append(d * power)
            n //= 10
            power *= 10
        return res[::-1]