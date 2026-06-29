class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -(2**31), 2**31 - 1
        i = 0
        n = len(s)

        # Step 1: Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Determine sign
        sign = 1
        if i < n and s[i] in ('+', '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Step 3: Read digits, skipping leading zeros implicitly
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # Step 4: Check overflow BEFORE updating result
            if result > (INT_MAX - digit) // 10:
                return INT_MIN if sign == -1 else INT_MAX

            result = result * 10 + digit
            i += 1

        return sign * result