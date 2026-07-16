class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return [x for x, c in Counter(nums).items() if c == 2]