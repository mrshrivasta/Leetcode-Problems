
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        for i in range(0, len(nums), 3):
            if len(nums[i:]) == len(set(nums[i:])):
                return i // 3
        return (len(nums) + 2) // 3
