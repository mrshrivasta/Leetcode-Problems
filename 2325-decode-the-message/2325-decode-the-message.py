class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        seen, table = set(), {}
        i = 0
        for c in key:
            if c != ' ' and c not in seen:
                table[c] = chr(ord('a') + i)
                seen.add(c)
                i += 1
        return ''.join(table.get(c, ' ') for c in message)