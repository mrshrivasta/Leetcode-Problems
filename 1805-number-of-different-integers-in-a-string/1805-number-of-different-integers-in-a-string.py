class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        import re
        return len(set(int(n) for n in re.split('[a-z]+', word) if n))