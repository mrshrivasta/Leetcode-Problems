class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, max_len = 0, 1

        def expand(left: int, right: int) -> None:
            nonlocal start, max_len

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            # Window has shrunk by 1 on each side after the loop exits
            length = right - left - 1
            if length > max_len:
                max_len = length
                start = left + 1

        for i in range(len(s)):
            expand(i, i)      # Odd-length  e.g. "aba"
            expand(i, i + 1)  # Even-length e.g. "abba"

        return s[start : start + max_len]