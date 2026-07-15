class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total, left, res = sum(nums), 0, 0
        for i in range(len(nums)-1):
            left += nums[i]
            if (left - (total - left)) % 2 == 0: res += 1
        return res