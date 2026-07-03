class Solution:
    def numSubarraysWithSum(self, nums, goal):
        from collections import defaultdict

        prefix = defaultdict(int)
        prefix[0] = 1

        s = 0
        ans = 0

        for x in nums:
            s += x
            ans += prefix[s - goal]
            prefix[s] += 1

        return ans