class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        # Build suffix sum: total shifts applied to each position
        total = 0
        suffix = [0] * len(s)
        for i in range(len(s) - 1, -1, -1):
            total += shifts[i]
            suffix[i] = total

        return ''.join(
            chr((ord(c) - ord('a') + suffix[i]) % 26 + ord('a'))
            for i, c in enumerate(s)
        )