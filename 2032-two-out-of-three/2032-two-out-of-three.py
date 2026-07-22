class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        return [x for x in range(1, 101) if (x in nums1) + (x in nums2) + (x in nums3) >= 2]