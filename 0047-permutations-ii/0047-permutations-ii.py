class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def backtrack(start: int) -> None:
            if start == len(nums):
                result.append(nums[:])
                return

            seen = set()   # values already tried at this position/depth

            for i in range(start, len(nums)):
                if nums[i] in seen:
                    continue               # same value already explored at this depth

                seen.add(nums[i])
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return result