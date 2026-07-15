class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, x in enumerate(nums):
            if sum(int(d) for d in str(x)) == i:
                return i
        return -1