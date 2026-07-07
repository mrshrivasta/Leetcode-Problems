class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        prev_size = 0
        for i, n in enumerate(nums):
            start = prev_size if i > 0 and nums[i] == nums[i-1] else 0
            prev_size = len(res)
            res += [s + [n] for s in res[start:prev_size]]
        return res