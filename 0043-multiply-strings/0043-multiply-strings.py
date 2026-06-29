class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n   = len(num1), len(num2)
        result = [0] * (m + n)   # product has at most m+n digits

        # Multiply each digit pair and accumulate
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1, p2 = i + j, i + j + 1   # positions in result array

                total       = mul + result[p2]
                result[p2]  = total % 10
                result[p1] += total // 10    # carry propagates left

        # Strip leading zeros and build string
        result_str = "".join(map(str, result)).lstrip("0")
        return result_str or "0"