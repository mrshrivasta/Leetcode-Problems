class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_element = min(nums)
        
        # Calculate sum(nums[i] - min_element) for all elements
        return sum(val - min_element for val in nums)