class Solution:
    def findMaxLength(self, nums):
        prefix = {0: -1}
        ans = 0
        s = 0

        for i, x in enumerate(nums):
            s += 1 if x == 1 else -1

            if s in prefix:
                ans = max(ans, i - prefix[s])
            else:
                prefix[s] = i

        return ans