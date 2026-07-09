from collections import Counter

class Solution:
    def maxEqualFreq(self, nums):
        cnt = Counter()
        freq = Counter()
        ans = maxFreq = 0

        for i, x in enumerate(nums, 1):
            if cnt[x]:
                freq[cnt[x]] -= 1

            cnt[x] += 1
            f = cnt[x]
            freq[f] += 1
            maxFreq = max(maxFreq, f)

            if (
                maxFreq == 1 or
                maxFreq * freq[maxFreq] + 1 == i or
                (maxFreq - 1) * (freq[maxFreq - 1] + 1) + 1 == i
            ):
                ans = i

        return ans