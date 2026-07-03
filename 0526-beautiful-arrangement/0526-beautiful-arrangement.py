class Solution:
    def countArrangement(self, n):
        self.ans = 0
        used = [False] * (n + 1)

        def dfs(pos):
            if pos > n:
                self.ans += 1
                return

            for num in range(1, n + 1):
                if not used[num] and (num % pos == 0 or pos % num == 0):
                    used[num] = True
                    dfs(pos + 1)
                    used[num] = False

        dfs(1)
        return self.ans