class Solution:
    def summaryRanges(self, nums):
        result = []
        i = 0
        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1
            if nums[i] != start:
                result.append(f"{start}->{nums[i]}")
            else:
                result.append(str(start))
            i += 1
        return result