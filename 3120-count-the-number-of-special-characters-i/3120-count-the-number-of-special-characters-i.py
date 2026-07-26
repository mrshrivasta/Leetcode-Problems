class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        return sum(c in word and c.upper() in word for c in set(word.lower()))