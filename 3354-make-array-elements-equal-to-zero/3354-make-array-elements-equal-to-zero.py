class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total, res = sum(nums), 0
        left = 0
        for i, x in enumerate(nums):
            if x == 0:
                right = total - left
                if left == right: res += 2
                elif abs(left - right) == 1: res += 1
            else:
                left += x
        return res