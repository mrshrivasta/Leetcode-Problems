class Solution:
    def sortString(self, s: str) -> str:
        count = Counter(s)
        result = []
        while len(result) < len(s):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if count[c]:
                    result.append(c)
                    count[c] -= 1
            for c in 'zyxwvutsrqponmlkjihgfedcba':
                if count[c]:
                    result.append(c)
                    count[c] -= 1
        return "".join(result)