class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        return [x for x, _ in Counter(nums).most_common(k)]