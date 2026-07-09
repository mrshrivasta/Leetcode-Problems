class Solution:
    def minKBitFlips(self, nums, k):
        n = len(nums)
        is_flipped = [0] * n
        flip = 0
        ans = 0

        for i in range(n):

            # Remove effect of flip that ended
            if i >= k:
                flip ^= is_flipped[i - k]

            # Current bit after all active flips
            if nums[i] == flip:
                if i + k > n:
                    return -1

                ans += 1
                flip ^= 1
                is_flipped[i] = 1

        return ans