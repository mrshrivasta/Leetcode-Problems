class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        count = 0
        for i, j, k in combinations(range(len(nums)), 3):
            if nums[i] != nums[j] and nums[j] != nums[k] and nums[i] != nums[k]:
                count += 1
        return count