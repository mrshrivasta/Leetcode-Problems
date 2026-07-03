class Solution:
    def checkSubarraySum(self, nums, k):
        prefix_mod = {0: -1}
        s = 0

        for i, x in enumerate(nums):
            s += x
            if k != 0:
                s %= k

            if s in prefix_mod:
                if i - prefix_mod[s] > 1:
                    return True
            else:
                prefix_mod[s] = i

        return False