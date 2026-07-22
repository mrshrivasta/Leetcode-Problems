class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for x in range(len(nums) + 1):
            if sum(n >= x for n in nums) == x:
                return x
        return -1