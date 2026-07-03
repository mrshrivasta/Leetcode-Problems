class Solution:
    def maximumUniqueSubarray(self, nums):
        seen = set()
        l = 0
        cur = 0
        ans = 0

        for r in range(len(nums)):
            while nums[r] in seen:
                seen.remove(nums[l])
                cur -= nums[l]
                l += 1

            seen.add(nums[r])
            cur += nums[r]
            ans = max(ans, cur)

        return ans