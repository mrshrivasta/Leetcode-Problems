class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        pool = Counter(chars)
        return sum(len(w) for w in words if not (Counter(w) - pool))