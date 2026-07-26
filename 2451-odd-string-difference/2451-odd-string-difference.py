class Solution:
    def oddString(self, words: list[str]) -> str:
        def diff(w):
            return [ord(w[i+1]) - ord(w[i]) for i in range(len(w)-1)]
        d = [diff(w) for w in words]
        for i, w in enumerate(words):
            if d.count(d[i]) == 1:
                return w