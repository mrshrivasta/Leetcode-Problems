class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        ones = [i for i, x in enumerate(nums) if x == 1]
        twos = [i for i, x in enumerate(nums) if x == 2]
        if not ones or not twos:
            return -1
        return min(abs(i - j) for i in ones for j in twos)