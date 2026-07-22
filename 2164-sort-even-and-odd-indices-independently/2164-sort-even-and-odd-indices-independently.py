class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        evens = sorted(nums[::2])
        odds = sorted(nums[1::2], reverse=True)
        nums[::2] = evens
        nums[1::2] = odds
        return nums