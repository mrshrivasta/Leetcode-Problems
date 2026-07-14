from collections import Counter

class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        return sum(v * cnt for v, cnt in c.items() if cnt % k == 0)