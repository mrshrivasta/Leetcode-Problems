class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(x for x, c in Counter(nums).items() if c == 1)