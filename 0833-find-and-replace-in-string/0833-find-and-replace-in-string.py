class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # Sort operations by index descending so replacements don't shift positions
        ops = sorted(zip(indices, sources, targets), reverse=True)

        for idx, src, tgt in ops:
            if s[idx:idx+len(src)] == src:
                s = s[:idx] + tgt + s[idx+len(src):]

        return s