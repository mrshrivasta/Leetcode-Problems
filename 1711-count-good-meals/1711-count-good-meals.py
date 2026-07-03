class Solution:
    def countPairs(self, deliciousness):
        MOD = 10**9 + 7
        freq = {}
        ans = 0

        for x in deliciousness:
            for p in range(22):
                target = (1 << p) - x
                if target in freq:
                    ans = (ans + freq[target]) % MOD

            freq[x] = freq.get(x, 0) + 1

        return ans