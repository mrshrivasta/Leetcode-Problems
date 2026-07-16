class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s = sum(nums)
        single = sum(x for x in nums if x < 10)
        double = s - single
        return single != double