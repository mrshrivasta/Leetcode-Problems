class Solution:
    def numberOfSubarrays(self, nums, k):
        from collections import defaultdict

        count = defaultdict(int)
        count[0] = 1

        odds = 0
        ans = 0

        for x in nums:
            if x % 2:
                odds += 1

            ans += count[odds - k]
            count[odds] += 1

        return ans