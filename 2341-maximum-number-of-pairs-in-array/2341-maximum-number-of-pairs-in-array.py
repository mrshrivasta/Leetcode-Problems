class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pairs = sum(v // 2 for v in Counter(nums).values())
        return [pairs, len(nums) - 2 * pairs]