class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = list(accumulate(nums))
        return [bisect_right(prefix, q) for q in queries]