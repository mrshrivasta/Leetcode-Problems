class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def next_valid(string, idx):
            skip = 0
            while idx >= 0:
                if string[idx] == '#':
                    skip += 1
                    idx -= 1
                elif skip > 0:
                    skip -= 1
                    idx -= 1
                else:
                    break
            return idx

        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0:
            i = next_valid(s, i)
            j = next_valid(t, j)

            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            if (i >= 0) != (j >= 0):
                return False

            i -= 1
            j -= 1

        return True