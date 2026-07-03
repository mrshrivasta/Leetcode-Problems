class Solution:
    def maxLength(self, arr):
        masks = []

        for s in arr:
            mask = 0
            ok = True
            for ch in s:
                bit = 1 << (ord(ch) - ord('a'))
                if mask & bit:
                    ok = False
                    break
                mask |= bit
            if ok:
                masks.append(mask)

        best = 0

        def dfs(i, cur):
            nonlocal best
            best = max(best, bin(cur).count("1"))

            for j in range(i, len(masks)):
                if cur & masks[j] == 0:
                    dfs(j + 1, cur | masks[j])

        dfs(0, 0)
        return best