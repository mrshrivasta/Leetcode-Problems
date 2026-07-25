class Solution:
    def dominantIndex(self, nums):
        idx = nums.index(max(nums))
        return idx if all(nums[idx] >= 2 * nums[i] for i in range(len(nums)) if i != idx) else -1