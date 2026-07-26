class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        return sum(sub.count('0') <= k or sub.count('1') <= k 
                   for i in range(len(s)) for j in range(i+1, len(s)+1) 
                   for sub in [s[i:j]])