class Solution:
    def findUnsortedSubarray(self, nums):
        n = len(nums)
        left, right = -1, -1

        max_seen = float('-inf')
        min_seen = float('inf')

        for i in range(n):
            if nums[i] < max_seen:
                right = i
            else:
                max_seen = nums[i]

        for i in range(n - 1, -1, -1):
            if nums[i] > min_seen:
                left = i
            else:
                min_seen = nums[i]

        return 0 if right == -1 else right - left + 1