class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        best = 0
        for i in range(len(s)):
            if s[i] == '0':
                zeros = ones = 0
                j = i
                while j < len(s) and s[j] == '0':
                    zeros += 1; j += 1
                while j < len(s) and s[j] == '1':
                    ones += 1; j += 1
                best = max(best, min(zeros, ones) * 2)
        return best