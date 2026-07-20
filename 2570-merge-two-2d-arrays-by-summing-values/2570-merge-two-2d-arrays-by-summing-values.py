class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        for id, val in nums1 + nums2:
            d[id] += val
        return sorted(d.items())