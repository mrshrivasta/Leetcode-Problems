class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        n, res = len(nums), 0
        for i in range(n):
            left = nums[i] > nums[i-k] if i-k >= 0 else True
            right = nums[i] > nums[i+k] if i+k < n else True
            if left and right:
                res += nums[i]
        return res