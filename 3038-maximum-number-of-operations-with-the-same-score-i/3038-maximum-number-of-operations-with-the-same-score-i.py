class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        target, count = nums[0] + nums[1], 0
        for i in range(0, len(nums)-1, 2):
            if nums[i] + nums[i+1] == target: count += 1
            else: break
        return count