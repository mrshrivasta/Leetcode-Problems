class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        for i in range(len(s) - k + 1):
            sub = s[i:i+k]
            if len(set(sub)) == 1:
                before = s[i-1] if i > 0 else None
                after = s[i+k] if i+k < len(s) else None
                if before != sub[0] and after != sub[0]:
                    return True
        return False