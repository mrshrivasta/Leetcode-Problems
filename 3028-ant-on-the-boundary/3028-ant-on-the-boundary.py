class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        pos = count = 0
        for x in nums:
            pos += x
            count += pos == 0
        return count