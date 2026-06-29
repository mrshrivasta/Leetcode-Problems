class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]  # any valid starting sum

        for i in range(len(nums) - 2):
            # Skip duplicate fixed elements (optional optimisation)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(total - target) < abs(closest - target):
                    closest = total

                if total == target:
                    return total          # can't get closer than exact
                elif total < target:
                    left += 1            # sum too small, move left up
                else:
                    right -= 1           # sum too large, move right down

        return closest