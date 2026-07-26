class Solution:
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
        seen, pairs = set(), 0
        for w in words:
            if w[::-1] in seen:
                pairs += 1
            seen.add(w)
        return pairs