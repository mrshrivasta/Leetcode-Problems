from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        words = set(wordDict)

        @lru_cache(maxsize=None)
        def dp(start):
            if start == len(s):
                return [""]
            res = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in words:
                    for rest in dp(end):
                        res.append(word + (" " + rest if rest else ""))
            return res

        return dp(0)