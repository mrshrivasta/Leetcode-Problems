class Solution:
    def subarraySum(self, nums, k):
        prefix = {0: 1}
        s = 0
        ans = 0

        for x in nums:
            s += x
            ans += prefix.get(s - k, 0)
            prefix[s] = prefix.get(s, 0) + 1

        return ans