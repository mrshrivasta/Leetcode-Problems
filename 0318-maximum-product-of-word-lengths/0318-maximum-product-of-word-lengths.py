class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = [0] * len(words)
        for i, w in enumerate(words):
            for c in w:
                masks[i] |= 1 << (ord(c)-ord('a'))
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if masks[i] & masks[j] == 0:
                    res = max(res, len(words[i])*len(words[j]))
        return res