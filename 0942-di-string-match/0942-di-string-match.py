class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        lo, hi = 0, len(s)
        result = []
        for c in s:
            if c == 'I':
                result.append(lo)
                lo += 1
            else:
                result.append(hi)
                hi -= 1
        result.append(lo)
        return result