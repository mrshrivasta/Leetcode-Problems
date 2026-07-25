class Solution:
    def largestEven(self, s: str) -> str:
        i = s.rfind('2')
        return s[:i+1] if i != -1 else ""