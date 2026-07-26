class Solution:
    def possibleStringCount(self, word: str) -> int:
        return 1 + sum(word[i] == word[i-1] for i in range(1, len(word)))