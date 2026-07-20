class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        return len(set().union(*[range(s, e+1) for s, e in nums]))