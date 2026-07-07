class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = cur_max = cur_min = nums[0]
        for n in nums[1:]:
            cur_max, cur_min = max(n, cur_max*n, cur_min*n), min(n, cur_max*n, cur_min*n)
            res = max(res, cur_max)
        return res