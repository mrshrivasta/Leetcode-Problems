from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            w = word[:i] + word[i+1:]
            if len(set(Counter(w).values())) == 1:
                return True
        return False