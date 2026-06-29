class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start: int) -> None:
            if start == len(nums):
                result.append(nums[:])
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]   # choose
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]   # undo

        backtrack(0)
        return result