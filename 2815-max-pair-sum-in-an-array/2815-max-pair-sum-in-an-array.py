class Solution:
    def maxSum(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for x in nums:
            d[max(int(c) for c in str(x))].append(x)
        return max((sum(sorted(v)[-2:]) for v in d.values() if len(v) >= 2), default=-1)