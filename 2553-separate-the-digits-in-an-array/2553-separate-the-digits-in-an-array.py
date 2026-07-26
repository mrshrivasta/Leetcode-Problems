class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(d) for x in nums for d in str(x)]