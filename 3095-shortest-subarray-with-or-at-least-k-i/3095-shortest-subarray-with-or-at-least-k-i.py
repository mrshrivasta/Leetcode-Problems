class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n, res = len(nums), float('inf')
        for i in range(n):
            val = 0
            for j in range(i, n):
                val |= nums[j]
                if val >= k:
                    res = min(res, j - i + 1)
                    break
        return res if res != float('inf') else -1