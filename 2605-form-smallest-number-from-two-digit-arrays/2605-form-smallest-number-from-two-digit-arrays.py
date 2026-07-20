class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        common = set(nums1) & set(nums2)
        if common: return min(common)
        a, b = min(nums1), min(nums2)
        return min(10*a+b, 10*b+a)