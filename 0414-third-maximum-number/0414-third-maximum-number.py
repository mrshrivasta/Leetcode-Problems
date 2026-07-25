class Solution:
    def thirdMax(self, nums):
        unique = sorted(set(nums), reverse=True)
        return unique[2] if len(unique) >= 3 else unique[0]