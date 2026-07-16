class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def inc(i): return all(nums[i+j] < nums[i+j+1] for j in range(k-1))
        return any(inc(i) and inc(i+k) for i in range(len(nums)-2*k+1))