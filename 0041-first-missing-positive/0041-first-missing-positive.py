class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Phase 1: Place each value v in its "home" slot (index v-1)
        # Only values in [1, n] have a valid home
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct = nums[i] - 1             # home index for nums[i]
                nums[i], nums[correct] = nums[correct], nums[i]

        # Phase 2: First index where the value is wrong = answer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1   # all of [1..n] present → answer is n+1