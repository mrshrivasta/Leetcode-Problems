class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n, res = len(nums), float('inf')
        for i in range(n):
            for j in range(i+l, min(i+r+1, n+1)):
                s = sum(nums[i:j])
                if s > 0: res = min(res, s)
        return res if res != float('inf') else -1