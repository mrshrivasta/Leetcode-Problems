class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        odd_count = sum(freq % 2 for freq in Counter(s).values())
        return odd_count <= k <= len(s)