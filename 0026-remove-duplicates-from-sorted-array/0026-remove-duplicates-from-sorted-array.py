class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1  # next position to write a unique value

        for fast in range(1, len(nums)):
            if nums[fast] != nums[fast - 1]:  # new unique value found
                nums[slow] = nums[fast]
                slow += 1

        return slow