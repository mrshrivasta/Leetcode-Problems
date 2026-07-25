class Solution:
    def reverseByType(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()][::-1]
        specials = [c for c in s if not c.isalpha()][::-1]
        res = list(s)
        li, si = 0, 0
        for i in range(len(res)):
            if res[i].isalpha():
                res[i] = letters[li]; li += 1
            else:
                res[i] = specials[si]; si += 1
        return ''.join(res)