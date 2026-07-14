class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd = sum(x % 2 for x in nums1)
        even = len(nums1) - odd
        # All even: even numbers stay even, odd numbers need odd-odd=even (need another odd)
        # All odd: odd numbers stay odd, even numbers need even-odd=odd (need an odd exists)
        return odd == 0 or even == 0 or odd >= 2 or (odd == 1 and even > 0)