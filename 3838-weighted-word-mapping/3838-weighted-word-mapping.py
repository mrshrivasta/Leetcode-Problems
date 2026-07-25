class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        res = ""
        for w in words:
            total = sum(weights[ord(c) - ord('a')] for c in w)
            res += chr(ord('z') - total % 26)
        return res