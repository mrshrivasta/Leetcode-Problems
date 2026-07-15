class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops = 0
        while any(nums[i] > nums[i+1] for i in range(len(nums)-1)):
            min_sum = min(nums[i]+nums[i+1] for i in range(len(nums)-1))
            for i in range(len(nums)-1):
                if nums[i]+nums[i+1] == min_sum:
                    nums = nums[:i] + [min_sum] + nums[i+2:]
                    break
            ops += 1
        return ops