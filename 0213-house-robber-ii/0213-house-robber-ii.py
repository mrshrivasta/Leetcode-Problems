class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(arr):
            p2 = p1 = 0
            for n in arr:
                p2, p1 = p1, max(p1, p2+n)
            return p1
        if len(nums) == 1: return nums[0]
        return max(rob1(nums[:-1]), rob1(nums[1:]))