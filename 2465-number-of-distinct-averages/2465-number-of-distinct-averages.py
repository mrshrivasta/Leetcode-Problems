class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        return len({nums[i] + nums[~i] for i in range(len(nums)//2)})