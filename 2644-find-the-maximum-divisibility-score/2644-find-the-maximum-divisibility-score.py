class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        return min(divisors, key=lambda d: (-sum(n % d == 0 for n in nums), d))