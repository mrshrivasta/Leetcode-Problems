class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -(2**31), 2**31 - 1

        # Only overflow case: -2^31 / -1 = 2^31, which exceeds INT_MAX
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Work in positives, apply sign at the end
        negative = (dividend < 0) != (divisor < 0)
        a = abs(dividend)
        b = abs(divisor)
        quotient = 0

        while a >= b:
            temp  = b
            multiple = 1

            while a >= (temp << 1):   # double temp until it would exceed a
                temp    <<= 1
                multiple <<= 1

            a        -= temp      # subtract largest fitting multiple
            quotient += multiple  # accumulate how many times b fits

        result = -quotient if negative else quotient
        return max(INT_MIN, min(INT_MAX, result))