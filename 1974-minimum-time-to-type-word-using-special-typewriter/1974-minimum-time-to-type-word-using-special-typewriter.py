class Solution:
    def minTimeToType(self, word: str) -> int:
        time, prev = 0, 0
        for c in word:
            curr = ord(c) - ord('a')
            diff = abs(curr - prev)
            time += min(diff, 26 - diff) + 1
            prev = curr
        return time