class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        from bisect import bisect_left
        tails = []
        for n in nums:
            i = bisect_left(tails, n)
            if i == len(tails): tails.append(n)
            else: tails[i] = n
        return len(tails)