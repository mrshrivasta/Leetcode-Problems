class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        return [w for w in words if any(w in other for other in words if w != other)]