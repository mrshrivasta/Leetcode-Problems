class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:-1]  # strip parentheses

        def valid_forms(t):
            # Returns all valid representations of digit string t
            results = []
            # Integer form: no leading zeros unless single '0'
            if t == '0' or not t.startswith('0'):
                results.append(t)
            # Decimal forms: split at each position
            for i in range(1, len(t)):
                left, right = t[:i], t[i:]
                # left: no leading zeros unless single digit
                # right: no trailing zeros
                if (left == '0' or not left.startswith('0')) and not right.endswith('0'):
                    results.append(left + '.' + right)
            return results

        result = []
        for split in range(1, len(s)):
            left_str, right_str = s[:split], s[split:]
            for l in valid_forms(left_str):
                for r in valid_forms(right_str):
                    result.append(f"({l}, {r})")

        return result