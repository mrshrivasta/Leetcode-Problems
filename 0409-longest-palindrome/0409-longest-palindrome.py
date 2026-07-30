class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        length = 0
        odd_found = False
        for v in count.values():
            length += v // 2 * 2
            if v % 2 == 1:
                odd_found = True
        return length + (1 if odd_found else 0)