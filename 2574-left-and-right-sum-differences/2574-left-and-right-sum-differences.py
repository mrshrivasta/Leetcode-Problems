class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left, right = 0, sum(nums)
        res = []
        for x in nums:
            right -= x
            res.append(abs(left - right))
            left += x
        return res