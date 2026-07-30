class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev, curr, count = 0, 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr += 1
            else:
                prev = curr
                curr = 1
            if prev >= curr:
                count += 1
        return count