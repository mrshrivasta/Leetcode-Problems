class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = {}
        result = -1
        for i, c in enumerate(s):
            if c in first:
                result = max(result, i - first[c] - 1)
            else:
                first[c] = i
        return result