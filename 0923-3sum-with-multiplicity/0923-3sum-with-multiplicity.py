class Solution:
    def threeSumMulti(self, arr, target):
        MOD = 10**9 + 7
        cnt = [0] * 101

        for x in arr:
            cnt[x] += 1

        ans = 0

        for i in range(101):
            for j in range(i, 101):
                k = target - i - j
                if 0 <= k <= 100:
                    if i == j == k:
                        ans += cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) // 6
                    elif i == j != k:
                        ans += cnt[i] * (cnt[i] - 1) // 2 * cnt[k]
                    elif i < j < k:
                        ans += cnt[i] * cnt[j] * cnt[k]

        return ans % MOD