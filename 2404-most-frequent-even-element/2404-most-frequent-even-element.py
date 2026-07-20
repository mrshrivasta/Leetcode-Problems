class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count = Counter(x for x in nums if x % 2 == 0)
        return min(count, key=lambda x: (-count[x], x)) if count else -1