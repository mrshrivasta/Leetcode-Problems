class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        start = 0

        for end in range(1, len(s) + 1):
            if end == len(s) or s[end] != s[start]:
                if end - start >= 3:
                    result.append([start, end - 1])
                start = end

        return result