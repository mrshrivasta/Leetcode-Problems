class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sums = [nums[i] + nums[i+1] for i in range(len(nums)-1)]
        return len(sums) != len(set(sums))