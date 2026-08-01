class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines, current = 1, 0

        for c in s:
            w = widths[ord(c) - ord('a')]
            if current + w > 100:
                lines += 1
                current = w
            else:
                current += w

        return [lines, current]