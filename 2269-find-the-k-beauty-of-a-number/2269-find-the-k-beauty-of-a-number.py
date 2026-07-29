class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        return sum(1 for i in range(len(s)-k+1) if int(s[i:i+k]) and num % int(s[i:i+k]) == 0)